from cryptography import fernet
from cryptography.fernet import Fernet

key=Fernet.generate_key()
file=open('Cryptography/encryption_key.txt',"wb")
file.write(key)
file.close()