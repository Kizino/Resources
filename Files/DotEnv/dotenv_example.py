# pip3 install python-dotenv
import os
from dotenv import load_dotenv
load_dotenv()

USERID = os.getenv("USERID")
PASSSWORD = os.getenv("PASSWORD")

if __name__ == "__main__":
    print(f'UserId: {USERID}')
    print(f'Password: {PASSSWORD}')