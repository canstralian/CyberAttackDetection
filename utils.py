import json
from prompts import PROMPTS

def get_prompt(vulnerability_type):
    """
    Fetch the prompt for a specific vulnerability type.
    """
    return PROMPTS.get(vulnerability_type, "No prompt available for this type.")

def save_results(output, file_name="results.json"):
    """
    Save the results to a JSON file.
    """
    with open(file_name, "w") as file:
        json.dump(output, file, indent=4)
    print(f"Results saved to {file_name}")
