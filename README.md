---
license: mit
language:
- en
auto_detected: true
datasets:
- Canstralian/pentesting_dataset
- Canstralian/Wordlists
- Canstralian/ShellCommands
- Canstralian/CyberExploitDB
- Chemically-motivated/CyberSecurityDataset
- Chemically-motivated/AI-Agent-Generating-Tool-Debugging-Prompt-Library
metrics:
- accuracy
- precision
- f1
- code_eval
base_model:
- WhiteRabbitNeo/WhiteRabbitNeo-33B-v1.5
---

# CyberAttackDetection

## Overview

The **CyberAttackDetection** model is a fine-tuned BERT-based sequence classification model designed to identify cyberattacks in textual descriptions. It classifies input data into two categories:  
- **Attack (1)**: The text describes a cybersecurity threat or attack.  
- **Non-Attack (0)**: The text does not describe a cybersecurity threat.

---

## Model Details

- **License**: [MIT License](LICENSE)
- **Datasets**:  
  - Custom cybersecurity datasets:  
    - `Canstralian/pentesting_dataset`  
    - `Canstralian/Wordlists`  
    - `Canstralian/ShellCommands`  
    - `Canstralian/CyberExploitDB`  
    - `Chemically-motivated/CyberSecurityDataset`  
    - `Chemically-motivated/AI-Agent-Generating-Tool-Debugging-Prompt-Library`  
- **Language**: English  
- **Metrics**:  
  - **Accuracy**: 85%  
  - **F1 Score**: 0.83  
  - **Precision**: 0.80  
  - **Recall**: 0.87  
- **Base Model**: `WhiteRabbitNeo/WhiteRabbitNeo-33B-v1.5`  
- **Pipeline Tag**: `text-classification`  
- **Library Name**: `transformers`  
- **Tags**: `cybersecurity`, `text-classification`, `attack-detection`, `BERT`  
- **New Version**: `v1.0.0`  
- **Auto-Detected Features**: True  

---

## Model Usage

### Installation
Before using the model, ensure the necessary dependencies are installed:  
```bash
pip install transformers torch
```

### Example Code
Use the following Python code to load the model and classify a sample text:

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
print(f"Prediction: {'Attack' if prediction.item() == 1 else 'Non-Attack'}")
```

---

## Model Training Details

### Training Objective
The model was fine-tuned to classify descriptive text as either an attack or non-attack event. It uses a **binary classification** approach.

### Training Data
- The training data includes cybersecurity-related attack descriptions and non-attack examples from curated datasets.

---

## Evaluation

The model was evaluated on a balanced test set using the following metrics:  
- **Accuracy**: 85%  
- **F1 Score**: 0.83  
- **Precision**: 0.80  
- **Recall**: 0.87  

These results indicate strong performance in detecting cyberattacks from text.

---

## License

This project is licensed under the **MIT License**. Refer to the [LICENSE](LICENSE) file for details.

---

## How to Contribute

We welcome contributions!  
- **Submit Issues**: If you encounter problems, open an issue on the repository.  
- **Pull Requests**: Feel free to contribute code improvements or documentation updates.

---

## Contact

For further information or inquiries, contact: **canstralian@cybersecurity.com**