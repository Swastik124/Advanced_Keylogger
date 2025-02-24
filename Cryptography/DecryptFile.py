from cryptography import fernet
from cryptography.fernet import Fernet

from Project.Keylogger import clipboard_information_e, keys_information_e, encrypted_file_names

key="XSXYuAiGDHxtY1saJK0lUWrM2PtpjUSrY3GCWJWbF-c="

system_information_e="e_system.txt"
clipboard_information_e="e_clipboard.txt"
keys_information_e="e_key_logged.txt"

encrypted_files= [system_information_e,clipboard_information_e,keys_information_e]
count=0

for decrypting_file in encrypted_files:
    with open(encrypted_files[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted=fernet.decrypt(data)

    with open(encrypted_files[count], 'rb') as f:
        f.write(decrypted)

    count+=1