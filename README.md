# Advanced Keylogger Project

## Overview
This repository contains a Python-based keylogger designed for educational purposes and cybersecurity research. The keylogger captures keystrokes, clipboard data, system information, microphone audio, and screenshots. It encrypts the collected data and sends it to a specified email address.

**Disclaimer:** This project is intended for ethical use only. Do not use this software to violate privacy or laws. The author is not responsible for any misuse of this tool.

---

## Features
- **Keystroke Logging:** Records all keystrokes typed on the keyboard.
- **Clipboard Monitoring:** Captures clipboard content.
- **System Information:** Collects details about the system (e.g., OS, processor, IP addresses).
- **Microphone Recording:** Records audio from the microphone.
- **Screenshot Capture:** Takes periodic screenshots of the screen.
- **Data Encryption:** Encrypts all collected data using the `cryptography` library.
- **Email Delivery:** Sends encrypted files to a specified email address.

---

## Files in Repository
1. **Keylogger.py**: The main script for logging data and sending it via email.
2. **GenerationKey.py**: Generates an encryption key and saves it to `encryption_key.txt`.
3. **DecryptFile.py**: Decrypts encrypted log files using the encryption key.
4. **encryption_key.txt**: Stores the encryption key used for encrypting/decrypting data.

---

## Requirements
To run this project, you need:
- Python 3.x installed on your system.
- Required libraries:


- Gmail account with "App Passwords" enabled for secure email delivery.

---

## How to Use
### 1. Generate Encryption Key
Run `GenerationKey.py` to create an encryption key:


This will generate a file named `encryption_key.txt`.

### 2. Run Keylogger
Run `Keylogger.py` to start logging:


The script will collect data and send encrypted files to your configured email address.

### 3. Decrypt Logs
To decrypt the encrypted files, use `DecryptFile.py`:


Ensure `encryption_key.txt` is in the same directory as the script.

---

## Converting to Executable
You can convert `Keylogger.py` into an executable file using PyInstaller:


The executable will be generated in the `dist` folder.

---

## Security & Ethical Use Disclaimer
This project is strictly for educational purposes and ethical cybersecurity research. Unauthorized use of this software to compromise privacy or security is illegal and unethical. Always obtain explicit consent before using this tool on any system.

---

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## Contact
For questions or collaboration opportunities, feel free to reach out via GitHub or email at `forprojects124@gmail.com`.
