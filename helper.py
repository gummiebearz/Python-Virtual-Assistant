from dotenv import dotenv_values

# LOAD ENVIRONMENT VARIABLES FROM .env
configs = dotenv_values(".env_var")

# LOAD EMAILS FROM .emails
emails = dotenv_values(".emails")