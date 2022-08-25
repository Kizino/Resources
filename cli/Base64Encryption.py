import base64
import click

@click.group()
def cli():
    pass

@cli.command("encrypt")
@click.option("-m", "--message", "message", help="Message to encrypt")
def encode_b64(message:str):
    message_bytes = message.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    print(base64_bytes.decode("ascii"))

@cli.command("decrypt")
@click.option("-m", "--message", "message", help="Message to encrypt")
def decode_b64(message:str):
    base64_bytes = message.encode("ascii")
    message_bytes = base64.b64decode(base64_bytes)
    print(message_bytes.decode("ascii"))

if __name__ == "__main__":
    cli()
