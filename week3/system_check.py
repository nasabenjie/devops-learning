import os
import json
from datetime import datetime

# Gather system information
info = {
    "timestamp": str(datetime.now()),
    "current_user": os.getenv("USER"),
    "home_directory": os.getenv("HOME"),
    "current_directory": os.getcwd(),
    "files_in_current_dir": os.listdir(".")
}

# Print to screen
print("System Check Report")
print("===================")
for key, value in info.items():
    print(f"{key}: {value}")

# Save to JSON file
with open("system_report.json", "w") as f:
    json.dump(info, f, indent=4)

print("\nReport saved to system_report.json")
