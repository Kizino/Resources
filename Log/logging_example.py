import os
from datetime import datetime

def log_message(message):
    # Create a Log folder in current  directory if not exist
    path = os.getcwd() + "/Log/"
    if not os.path.exists(path):
        os.makedirs(path)

    # Compose Log Message
    log = f'[{datetime.now().strftime("%m/%d/%Y %H:%M:%S")}] - {message}\n'

    # Write Log Message to file
    with open(os.getcwd() + "/Log/log.txt", "a") as f:
        f.write(log)

def main():
    log_message("Starting Program")
    log_message("Exiting Program")

if __name__ == "__main__":
    main()