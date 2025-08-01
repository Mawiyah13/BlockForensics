from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Protocol.KDF import PBKDF2
import os

def decrypt_text(input_encrypted_path, output_dir, passkey):
    salt = b'\x00' * 16  
    key = PBKDF2(passkey, salt, dkLen=32)  

    with open(input_encrypted_path, 'rb') as f:
        iv = f.read(16)
        encrypted_data = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_data)
    unpadded_text_data = unpad(decrypted_data, AES.block_size)

    output_filename = os.path.basename(input_encrypted_path).replace('.enc', '')
    output_path = os.path.join(output_dir, output_filename)

    with open(output_path, 'wb') as f:
        f.write(unpadded_text_data)

    print(f'Text file decrypted and saved to: {output_path}')

if __name__ == "__main__":
    passkey = input("Enter the passkey for decryption: ")
    input_encrypted_path = 'encrypted_texts/input_text.txt.enc'
    output_dir = 'decrypted_texts'
    os.makedirs(output_dir, exist_ok=True)
    decrypt_text(input_encrypted_path, output_dir, passkey)
