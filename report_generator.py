import os
import sys
import datetime

# Get environment variables from Jenkins
author = os.environ.get('REPORT_AUTHOR', 'Unknown')
is_urgent = os.environ.get('IS_URGENT', 'false')

filename = "daily_report.txt"

print(f"--- Generating Report by {author} ---")

with open(filename, "w") as f:
    f.write(f"REPORT GENERATED ON: {datetime.datetime.now()}\n")
    f.write(f"AUTHOR: {author}\n")
    f.write(f"URGENT PRIORITY: {is_urgent}\n")
    f.write("--------------------------------------\n")
    f.write("Sales: 100%\n")
    f.write("Bugs: 0%\n")

print(f"Success! {filename} created.")
