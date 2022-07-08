# pip3 install python-dotenv
import os
from dotenv import load_dotenv
load_dotenv()

USERID = os.getenv("USERID")
PASSSWORD = os.getenv("PASSWORD")

def main():
    print(f'UserId: {USERID}')
    print(f'Password: {PASSSWORD}')

if __name__ == "__main__":
    main()