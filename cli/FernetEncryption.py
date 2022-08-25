import click
from cryptography.fernet import Fernet

@click.group()
def cli():
    pass

@cli.command("genkey")
def generate_encryption_key():
    key = Fernet.generate_key().decode()
    print(bytes(key, 'utf-8').decode())

@cli.command("decrypt")
@click.option("-m", "--message", "message", help="Message to encrypt")
@click.option("-k", "--key", "KEY", help="Key to encrypt")
def decrypt_message(message:str, KEY:str):
    key = bytes(KEY, 'utf-8')
    fernet = Fernet(key)

    decryptedMessage = fernet.decrypt(bytes(message, 'utf-8')).decode()
    print(decryptedMessage)

@cli.command("encrypt")
@click.option("-m", "--message", "message", help="Message to encrypt")
@click.option("-k", "--key", "KEY", help="Key to decrypt")
def encrypt_message(message:str, KEY:str):
    key = bytes(KEY, 'utf-8')
    fernet = Fernet(key)

    encryptedMessage = fernet.encrypt(bytes(message, 'utf-8')).decode()

    print(encryptedMessage)

if __name__ == '__main__':
    cli()

    
    
