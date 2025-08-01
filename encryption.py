from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Protocol.KDF import PBKDF2
import os

def encrypt_image(input_image_path, output_dir, passkey):
    salt = b'\x00' * 16  
    key = PBKDF2(passkey, salt, dkLen=32)  

    with open(input_image_path, 'rb') as f:
        image_data = f.read()

    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_image_data = pad(image_data, AES.block_size)
    encrypted_data = cipher.encrypt(padded_image_data)

    output_filename = os.path.basename(input_image_path) + '.enc'
    output_path = os.path.join(output_dir, output_filename)

    with open(output_path, 'wb') as f:
        f.write(iv)
        f.write(encrypted_data)

    print(f'Image encrypted and saved to: {output_path}')

if __name__ == "__main__":
    passkey = input("Enter the passkey for encryption: ")
    input_image_path = 'input_image.jpg'
    output_dir = 'encrypted_images'
    os.makedirs(output_dir, exist_ok=True)
    encrypt_image(input_image_path, output_dir, passkey)
