from nacl.bindings.crypto_aead import crypto_aead_xchacha20poly1305_ietf_encrypt
from nacl.bindings.crypto_aead import crypto_aead_xchacha20poly1305_ietf_decrypt

BLOCKS_SEPARATOR = '$'


def encrypt(message):
    encrypted = crypto_aead_xchacha20poly1305_ietf_encrypt()
    return f'{encrypted.hex()}{BLOCKS_SEPARATOR}{nonce.hex()}'


def decrypt(encrypted_message: str):
    encrypted, nonce = tuple(bytes.fromhex(block) for block in encrypted_message.split(BLOCKS_SEPARATOR))
    return crypto_aead_xchacha20poly1305_ietf_decrypt(encrypted, None, nonce, KeyProvider.get())
