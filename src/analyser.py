log_file = "logs/application.log"

info_count = 0
warning_count = 0
error_count = 0  

with open(log_file, "r") as file:
    for line in file:
        if "INFO" in line:
            info_count += 1
        elif "WARNING" in line:
            warning_count += 1
        elif "ERROR" in line:
            error_count += 1

print(f"INFO: {info_count}")
print(f"WARNING: {warning_count}")
print(f"ERROR: {error_count}")  
print("-------------------")
print("Log Analyzer Report")