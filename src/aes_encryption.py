from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os


# Function to read data from file
def read_data(file_path):
    with open(file_path, 'rb') as file:
        return file.read()


# Function to encrypt data using AES
def encrypt_data(data, key):
    iv = os.urandom(16)  # Generate a random IV (Initialization Vector)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return iv + encrypted_data


# Function to decrypt data using AES
def decrypt_data(encrypted_data, key):
    iv = encrypted_data[:16]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_data = decryptor.update(encrypted_data[16:]) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
    return unpadded_data


if __name__ == "__main__":
    key = os.urandom(32)
    data = read_data('../data/sample_data.txt')

    encrypted_data = encrypt_data(data, key)
    decrypted_data = decrypt_data(encrypted_data, key)

    print(f"Original Data: {data}")
    print(f"Encrypted Data: {encrypted_data}")
    print(f"Decrypted Data: {decrypted_data}")
