from dotenv import dotenv_values
import csv

# LOAD ENVIRONMENT VARIABLES FROM .env
configs = dotenv_values(".env_var")

# LOAD EMAILS FROM .emails.txt
try:
    emails = {}
    with open(configs["FILE_EMAILS"], "r") as email_file:
        for line in csv.reader(email_file, delimiter=","):
            if line[0] == 'name':
                continue

            name, email = line
            emails[name.strip().lower()] = email.strip().lower()
except:
    emails = {}
    print(f"*** ERROR: Could not open file {configs['FILE_EMAILS']}")

### LOAD UTILITIES FROM utilities.txt
try:
    with open(configs["FILE_UTILITIES"], "r") as utility_file:
        utilities = utility_file.read().replace("\n", ", ")
except:
    utilities = {}
    print(f"*** ERROR: Could not open file {configs['FILE_UTILITIES']}")