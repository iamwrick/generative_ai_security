import os

import matplotlib.pyplot as plt
import numpy as np
from aes_encryption import encrypt_data, decrypt_data

key = os.urandom(32)
data = b"Sensitive training data for generative AI"

encrypted_data = encrypt_data(data, key)
decrypted_data = decrypt_data(encrypted_data, key)

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.title('Original Training Data')
plt.plot(np.frombuffer(data, dtype=np.uint8), 'o-')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.title('Encrypted Training Data')
plt.plot(np.frombuffer(encrypted_data, dtype=np.uint8), 'o-')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.title('Decrypted Training Data')
plt.plot(np.frombuffer(decrypted_data, dtype=np.uint8), 'o-')
plt.grid(True)

plt.savefig('aes_encryption_process.png', dpi=300)
plt.tight_layout()
plt.show()
