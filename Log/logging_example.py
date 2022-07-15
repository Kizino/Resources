import os
from datetime import datetime

def logging(message):
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
    logging("Starting Program")
    logging("Exiting Program")

if __name__ == "__main__":
    main()