from nacl.bindings.crypto_aead import crypto_aead_xchacha20poly1305_ietf_encrypt
from nacl.bindings.crypto_aead import crypto_aead_xchacha20poly1305_ietf_decrypt
from django.conf import settings
from sensitive_data.key_manager import read_key, generate_nonce

BLOCKS_SEPARATOR = '$'
ENCODING = 'utf-8'


def encrypt(message: str):
    if not message:
        return message
    secret_key = read_key(settings.SENSITIVE_DATA_SECRET_KEY_FILE)
    nonce = generate_nonce()
    message_bytes = message.encode(ENCODING)
    encrypted = crypto_aead_xchacha20poly1305_ietf_encrypt(message_bytes, None, nonce, secret_key)
    return f'{encrypted.hex()}{BLOCKS_SEPARATOR}{nonce.hex()}'


def decrypt(encrypted_message: str):
    if not encrypted_message:
        return encrypted_message
    secret_key = read_key(settings.SENSITIVE_DATA_SECRET_KEY_FILE)
    encrypted, nonce = tuple(bytes.fromhex(block) for block in encrypted_message.split(BLOCKS_SEPARATOR))
    return crypto_aead_xchacha20poly1305_ietf_decrypt(encrypted, None, nonce, secret_key).decode(ENCODING)
