---
license: mit
language:
- en
datasets:
- Canstralian/pentesting_dataset
- Canstralian/Wordlists
- Canstralian/ShellCommands
- Canstralian/CyberExploitDB
- Chemically-motivated/CyberSecurityDataset
- Chemically-motivated/AI-Agent-Generating-Tool-Debugging-Prompt-Library
base_model:
- WhiteRabbitNeo/WhiteRabbitNeo-33B-v1.5
library_name: transformers
---

# CyberAttackDetection

This model is a fine-tuned BERT-based sequence classification model designed to detect cyberattacks in text. It classifies textual descriptions of cybersecurity events into two categories: **attack (1)** and **non-attack (0)**.

## Model Details

- **Model Type**: BERT-based sequence classification
- **Training Data**: Cybersecurity-related attack descriptions
- **Intended Use**: Detects potential cybersecurity threats in descriptive text data.
- **Fine-tuning Objective**: Classify descriptive text as either an attack or non-attack event.

## Model Usage

You can use this model to classify whether a given piece of text indicates a cyberattack. Below is an example of how to use the model in Python:

### Install Dependencies

Before using the model, make sure to install the necessary dependencies by running:

  ```bash
pip install -r requirements.txt
  ```
### Example Usage
  ```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Load the fine-tuned model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("Canstralian/CyberAttackDetection")
tokenizer = AutoTokenizer.from_pretrained("Canstralian/CyberAttackDetection")

# Example input: Cyberattack description
text = "A vulnerability was discovered in the server software."

# Tokenize the input
inputs = tokenizer(text, return_tensors="pt")

# Get model predictions
outputs = model(**inputs)

# Predict the label (1 = attack, 0 = non-attack)
prediction = outputs.logits.argmax(dim=-1)
print(f"Prediction: {'Attack' if prediction.item() == 1 else 'Non-attack'}")
  ```
## Model Training Details
This model was fine-tuned on a cybersecurity dataset containing attack descriptions. The model is trained to recognize patterns in textual descriptions of cybersecurity events and classify them accordingly.

## Evaluation
### Metrics: Accuracy, F1 Score, Precision, Recall.
The model was evaluated on a test set and achieved an accuracy of 85% in detecting cyberattacks from textual descriptions.
## License
This model is licensed under the MIT License.

## How to Contribute
Feel free to open issues or contribute to this repository. Pull requests are welcome.

## Contact
For further information or inquiries, contact the author at: canstralian@cybersecurity.com