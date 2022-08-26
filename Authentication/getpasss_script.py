# Documentation: https://docs.python.org/3/library/getpass.html
import getpass

if __name__ == "__main__":
    user = getpass.getuser()
    password = getpass.getpass(prompt="Password: ", stream=None)
    
    print(user)
    print(password)
