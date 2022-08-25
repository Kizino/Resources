import json
import click
import base64

with open(".config") as f:
    config = json.load(f)

def decode_b64(message : str):
    base64_bytes = message.encode("ascii")
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode("ascii")

@click.group()
def cli():
    pass

@cli.command()
@click.option("-k", "--key", "key", help="Key to encrypt")
def get(key: str):
    try:
        print(decode_b64(config.get(key)))
    except:
        print("The key entered is incorrect")

@cli.command()
def list():
    for key in config.keys():
        print(key)

if __name__ == "__main__":
    cli()
