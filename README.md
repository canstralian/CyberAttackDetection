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

## Prompts:
- Open Ports: "Analyze the following network scan report and identify open ports and their associated vulnerabilities. Suggest best practices to secure these ports: [Insert network scan report]."
- Outdated Software or Services: "Given this list of installed software and services, identify outdated versions and known vulnerabilities. Provide recommendations for updates or patches to mitigate risks: [Insert software and service list]."
- Default Credentials: "Scan the following system configurations for any use of default credentials. Provide a list of affected services and recommendations for securing these credentials: [Insert system configuration details]."
- Misconfigurations: "Evaluate the provided system configuration for potential misconfigurations. Highlight risks and provide recommendations for secure setup: [Insert system configuration details]."
- Injection Flaws: "Review the given web application code or request logs and identify potential injection vulnerabilities such as SQL injection, command injection, or XSS. Provide remediation steps: [Insert code or logs]."
- Unencrypted Services: "Analyze the following network configuration and identify services that are transmitting data without encryption. Suggest strategies to enforce secure transmission: [Insert network configuration details]."
- Known Software Vulnerabilities: "Review the provided software inventory and cross-reference it with known vulnerabilities in the National Vulnerability Database (NVD). Recommend patches or workarounds: [Insert software inventory]."
- Cross-Site Request Forgery (CSRF): "Examine the provided web application code for potential CSRF vulnerabilities. Suggest specific coding or configuration techniques to prevent these attacks: [Insert code]."
- Insecure Direct Object References (IDOR): "Analyze the provided API endpoints and their associated access controls. Identify any IDOR vulnerabilities and suggest secure implementation strategies: [Insert API endpoint details]."
- Security Misconfigurations in Web Servers/Applications: "Assess the given web server configuration for security misconfigurations, such as improper HTTP headers or verbose error messages. Recommend changes to harden the server: [Insert server configuration]."
- Broken Authentication and Session Management: "Review the provided authentication and session management implementation. Identify weaknesses and recommend strategies to prevent compromise: [Insert authentication/session management details]."
- Sensitive Data Exposure: "Analyze the system's data handling processes and storage practices to identify potential sensitive data exposure. Recommend measures to protect sensitive information: [Insert system details]."
- API Vulnerabilities: "Examine the following API documentation and implementation for vulnerabilities, including insecure endpoints and data leakage. Provide recommendations for securing the API: [Insert API documentation]."
- Denial of Service (DoS) Vulnerabilities: "Review the system's architecture and configuration for potential vulnerabilities to DoS attacks. Suggest mitigation strategies such as rate limiting and load balancing: [Insert system architecture]."
- Buffer Overflows: "Analyze the provided code or application for buffer overflow vulnerabilities. Highlight potential weak points and recommend secure coding practices to prevent exploitation: [Insert code]."


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