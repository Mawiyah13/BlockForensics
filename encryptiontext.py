from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Protocol.KDF import PBKDF2
import os

def create_text_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)
    print(f'Text file created and content written to: {file_path}')

def encrypt_text(input_text_path, output_dir, passkey):
    salt = b'\x00' * 16  
    key = PBKDF2(passkey, salt, dkLen=32)  

    with open(input_text_path, 'rb') as f:
        text_data = f.read()

    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text_data = pad(text_data, AES.block_size)
    encrypted_data = cipher.encrypt(padded_text_data)

    output_filename = os.path.basename(input_text_path) + '.enc'
    output_path = os.path.join(output_dir, output_filename)

    with open(output_path, 'wb') as f:
        f.write(iv)
        f.write(encrypted_data)

    print(f'Text file encrypted and saved to: {output_path}')

if __name__ == "__main__":
    file_path = 'input_text.txt'
    content = "This is a sample text to be encrypted."
    create_text_file(file_path, content)

    passkey = input("Enter the passkey for encryption: ")
    output_dir = 'encrypted_texts'
    os.makedirs(output_dir, exist_ok=True)
    encrypt_text(file_path, output_dir, passkey)
