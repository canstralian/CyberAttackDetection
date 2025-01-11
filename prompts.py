PROMPTS = {
    "open_ports": (
        "Analyze the following network scan report and identify open ports and their associated vulnerabilities. "
        "Suggest best practices to secure these ports: [Insert network scan report]."
    ),
    "outdated_software": (
        "Given this list of installed software and services, identify outdated versions and known vulnerabilities. "
        "Provide recommendations for updates or patches to mitigate risks: [Insert software and service list]."
    ),
    "default_credentials": (
        "Scan the following system configurations for any use of default credentials. Provide a list of affected services "
        "and recommendations for securing these credentials: [Insert system configuration details]."
    ),
    "misconfigurations": (
        "Evaluate the provided system configuration for potential misconfigurations. Highlight risks and provide "
        "recommendations for secure setup: [Insert system configuration details]."
    ),
    # Add more prompts as necessary
}
