from transformers import AutoTokenizer, AutoModelForCausalLM
from config import Config

class CyberAttackDetectionModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(Config.TOKENIZER_NAME)
        self.model = AutoModelForCausalLM.from_pretrained(Config.MODEL_NAME)
        self.model.to(Config.DEVICE)
    
    def predict(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True, max_length=Config.MAX_LENGTH)
        inputs = {key: value.to(Config.DEVICE) for key, value in inputs.items()}
        
        outputs = self.model.generate(**inputs, max_length=Config.MAX_LENGTH)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
