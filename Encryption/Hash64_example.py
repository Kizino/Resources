import base64

def encode_b64(message):
    message_bytes = message.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes.decode("ascii")

def decode_b64(message):
    base64_bytes = message.encode("ascii")
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode("ascii")

if __name__ == "__main__":
    print(f'Encoded message: {encode_b64("This is the way!")}')
    print(f'Decoded message: {decode_b64("VGhpcyBpcyB0aGUgd2F5IQ==")}')