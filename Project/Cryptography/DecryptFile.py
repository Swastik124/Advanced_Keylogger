from cryptography.fernet import Fernet
import os

key = "A92H10hAY7_QrpzcPwhxBJenri_7l7xKG6ealdhI_mk="
encrypted_files = [
    "e_systeminfo.txt",
    "e_clipboard.txt",
    "e_key_log.txt"
]

def decrypt_files():
    fernet = Fernet(key)
    for file in encrypted_files:
        if os.path.exists(file):
            with open(file, "rb") as f:
                encrypted_data = f.read()
            decrypted_data = fernet.decrypt(encrypted_data)
            original_name = file.replace("e_", "")
            with open(original_name, "wb") as f:
                f.write(decrypted_data)
            print(f"Decrypted {file} to {original_name}")

if __name__ == "__main__":
    decrypt_files()