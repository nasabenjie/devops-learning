errors = []
warnings = []

with open("sample.log", "r") as f:
    for line in f:
        line = line.strip()
        if "ERROR" in line:
            errors.append(line)
        elif "WARNING" in line:
            warnings.append(line)

# Print to screen
print(f"Found {len(errors)} errors and {len(warnings)} warnings")
print()

# Save report to file
with open("report.txt", "w") as f:
    f.write(f"LOG ANALYSIS REPORT\n")
    f.write(f"==================\n\n")
    f.write(f"Total errors: {len(errors)}\n")
    f.write(f"Total warnings: {len(warnings)}\n\n")
    f.write("ERRORS:\n")
    for error in errors:
        f.write(f"  {error}\n")
    f.write("\nWARNINGS:\n")
    for warning in warnings:
        f.write(f"  {warning}\n")

print("Report saved to report.txt")
