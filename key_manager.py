from nacl.bindings.crypto_aead import crypto_aead_xchacha20poly1305_ietf_encrypt
from nacl.bindings.crypto_aead import crypto_aead_xchacha20poly1305_ietf_decrypt

import sys

KEY_SIZE_BITS = 256
NONCE_SIZE_BITS = 192


def generate_random(csprng_source, bits):
    bytes_amount = bits // 8
    with(open(csprng_source, 'rb')) as f:
        return bytes(f.read(bytes_amount))


def generate_random_key(bits=KEY_SIZE_BITS):
    key_bytes = generate_random('/dev/random', bits)
    return int.from_bytes(key_bytes, byteorder=sys.byteorder)


def generate_nonce(bits=NONCE_SIZE_BITS):
    return generate_random('/dev/urandom', bits)


def key_to_bytes(key: int):
    return key.to_bytes(KEY_SIZE_BITS // 8, sys.byteorder)
