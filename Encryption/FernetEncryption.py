from cryptography.fernet import Fernet

def decrypt_message(encryptedMessage, KEY):
    key = bytes(KEY, 'utf-8')
    fernet = Fernet(key)

    decryptedMessage = fernet.decrypt(bytes(encryptedMessage, 'utf-8')).decode()
    print(decryptedMessage)

def encrypt_message(message, KEY):
    key = bytes(KEY, 'utf-8')
    fernet = Fernet(key)

    encryptedMessage = fernet.encrypt(bytes(message, 'utf-8')).decode()

    print(encryptedMessage)

def generate_encryption_key():
    key = Fernet.generate_key().decode()
    print(bytes(key, 'utf-8').decode())

if __name__ == '__main__':
    # Create new key if necessary
    # generate_encryption_key()

    # CONFIG
    KEY = "JZWn95esyzMPhryTx0XNezCYHVbIYiglPcLry9BpKAM="

    message_to_encrypt = "message"
    message_to_decrypt = "gAAAAABjB4iZ848bl08gCDmv2_UMVPQcGGfOl_vPrM2B5FFapxJ5zF9l27f8EZ1VlKTMrpwzDoT0PrvxgfzgswK7xy5buG1BzA=="

    encrypt_message(message_to_encrypt,KEY)
    decrypt_message(message_to_decrypt,KEY)
    
