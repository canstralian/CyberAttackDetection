import os

# Configuration for the CyberAttackDetection model
class Config:
    MODEL_NAME = "Canstralian/CyberAttackDetection"
    TOKENIZER_NAME = "Canstralian/CyberAttackDetection"
    MAX_LENGTH = 512
    DEVICE = "cuda" if os.environ.get("USE_CUDA", "1") == "1" else "cpu"
    PROMPTS_FILE = "prompts.py"
