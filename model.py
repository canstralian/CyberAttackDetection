from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from datasets import load_dataset, Dataset, DatasetDict
from config import Config
import torch
from sklearn.model_selection import train_test_split
import pandas as pd

class CyberAttackDetectionModel:
    def __init__(self):
        # Initialize tokenizer and model
        self.tokenizer = AutoTokenizer.from_pretrained(Config.TOKENIZER_NAME)
        self.model = AutoModelForCausalLM.from_pretrained(Config.MODEL_NAME)
        self.model.to(Config.DEVICE)
    
    def preprocess_data(self, dataset):
        """
        Preprocess the raw text dataset by cleaning and tokenizing.
        """
        # Clean the dataset (basic text normalization, removing unwanted characters)
        def clean_text(text):
            # Implement custom cleaning function based on dataset's characteristics
            # E.g., removing unwanted characters, special symbols, etc.
            text = text.lower()  # Example of making text lowercase
            text = text.replace("\n", " ")  # Removing newlines
            return text
        
        # Apply cleaning to the dataset
        dataset = dataset.map(lambda x: {'text': clean_text(x['text'])})
        
        # Tokenization
        def tokenize_function(examples):
            return self.tokenizer(examples['text'], truncation=True, padding='max_length', max_length=Config.MAX_LENGTH)
        
        # Tokenize the entire dataset
        tokenized_dataset = dataset.map(tokenize_function, batched=True)
        
        # Set format for PyTorch
        tokenized_dataset.set_format(type='torch', columns=['input_ids', 'attention_mask', 'labels'])
        
        return tokenized_dataset
    
    def fine_tune(self, datasets):
        """
        Fine-tune the model with the preprocessed datasets.
        """
        # Load datasets (after pre-processing)
        dataset_dict = DatasetDict({
            "train": datasets['train'],
            "validation": datasets['validation'],
        })
        
        # Training arguments
        training_args = TrainingArguments(
            output_dir=Config.OUTPUT_DIR,
            evaluation_strategy="epoch",
            learning_rate=Config.LEARNING_RATE,
            per_device_train_batch_size=Config.BATCH_SIZE,
            per_device_eval_batch_size=Config.BATCH_SIZE,
            weight_decay=Config.WEIGHT_DECAY,
            save_total_limit=3,
            num_train_epochs=Config.NUM_EPOCHS,
            logging_dir=Config.LOGGING_DIR,
            load_best_model_at_end=True
        )
        
        # Trainer
        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=dataset_dict['train'],
            eval_dataset=dataset_dict['validation'],
        )
        
        # Fine-tuning
        trainer.train()
    
    def predict(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True, max_length=Config.MAX_LENGTH)
        inputs = {key: value.to(Config.DEVICE) for key, value in inputs.items()}
        
        outputs = self.model.generate(**inputs, max_length=Config.MAX_LENGTH)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def load_and_process_datasets(self):
        """
        Loads and preprocesses the datasets for fine-tuning.
        """
        # Load your OSINT and WhiteRabbitNeo datasets
        osint_datasets = [
            'gonferspanish/OSINT', 
            'Inforensics/missing-persons-clue-analysis-osint',
            'jester6136/osint', 
            'originalbox/osint'
        ]
        
        wrn_datasets = [
            'WhiteRabbitNeo/WRN-Chapter-2',
            'WhiteRabbitNeo/WRN-Chapter-1',
            'WhiteRabbitNeo/Code-Functions-Level-Cyber'
        ]
        
        # Combine all datasets into one for training
        combined_datasets = []
        
        # Load and preprocess OSINT datasets
        for dataset_name in osint_datasets:
            dataset = load_dataset(dataset_name)
            processed_data = self.preprocess_data(dataset['train'])  # Assuming the 'train' split exists
            combined_datasets.append(processed_data)
        
        # Load and preprocess WhiteRabbitNeo datasets
        for dataset_name in wrn_datasets:
            dataset = load_dataset(dataset_name)
            processed_data = self.preprocess_data(dataset['train'])  # Assuming the 'train' split exists
            combined_datasets.append(processed_data)
        
        # Combine all preprocessed datasets
        full_dataset = DatasetDict()
        full_dataset['train'] = Dataset.from_dict(pd.concat([d['train'] for d in combined_datasets]))
        full_dataset['validation'] = Dataset.from_dict(pd.concat([d['validation'] for d in combined_datasets]))
        
        return full_dataset

if __name__ == "__main__":
    # Create the model object
    model = CyberAttackDetectionModel()

    # Load and preprocess datasets
    preprocessed_datasets = model.load_and_process_datasets()

    # Fine-tune the model
    model.fine_tune(preprocessed_datasets)

    # Example prediction
    prompt = "A network scan reveals an open port 22 with an outdated SSH service."
    print(model.predict(prompt))
