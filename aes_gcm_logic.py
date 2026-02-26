from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

# This script simulates the core cryptographic logic of my M.Sc. Thesis [cite: 20]
def encrypt_sensitive_data(data, key):
    # AES-GCM requires a 96-bit nonce for security [cite: 52]
    nonce = os.urandom(12)
    aesgcm = AESGCM(key)
    # Encrypts and provides an authentication tag (AEAD) [cite: 52, 124]
    ciphertext = aesgcm.encrypt(nonce, data.encode(), None)
    return nonce, ciphertext

if __name__ == "__main__":
    # Example key (32 bytes for AES-256)
    key = AESGCM.generate_key(bit_length=256)
    nonce, encrypted = encrypt_sensitive_data("Sensitive Smartphone Data", key)
    print(f"Nonce: {nonce.hex()}\nCiphertext: {encrypted.hex()}")
