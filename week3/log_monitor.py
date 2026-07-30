import json

errors = []
warnings = []

with open("app.log", "r") as f:
    for line in f:
        line = line.strip()
        if "ERROR" in line:
            errors.append(line)
        elif "WARNING" in line:
            warnings.append(line)

print(f"Found {len(errors)} errors and {len(warnings)} warnings")
print()

info = {
    "total_errors": len(errors),
    "total_warnings": len(warnings),
    "error_messages": errors,
    "warning_messages": warnings
}

with open("log_summary.json", "w") as f:
    json.dump(info, f, indent=4)

print("Report saved to log_summary.json")
