import getpass,time,logging,random
import uuid,progressbar, os
newpath = r'C:\Arb'
if not os.path.exists(newpath):
    os.makedirs(newpath)

if os.path.exists(newpath):
    if not os.path.exists(r"C:\Arb\log.log"):
        h = open(r"C:\Arb\log.log", "a+")
        h.close()
import logging
logging.basicConfig(filename='C:\Arb\log.log',level=logging.DEBUG)
logging.debug('Start of the Main Program')
logging.debug("\n")



def p():
    print(Fore.GREEN + """
  _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _  
 / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
( E | N | C | R | Y | P | T | I | O | N | D | E | C | R | Y | P | T | I | O | N )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
                                                                                                       """)
    print(Style.RESET_ALL)
def auth():
    print(Fore.RED + "a???s? ?a?e:?as? saxe?a(???4?s!?_?473?)")
    print(Style.RESET_ALL)

import colorama, time
from colorama import Fore, Style
colorama.init()
x = uuid.getnode()
c = str(x)
p()
auth()
import random
import secrets
import string
import datetime
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
def mail():
    c = True
    while c:
        try:
            fromaddr = "cyberbot1502@gmail.com"
            toaddr = "cyberbot1502@gmail.com"
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = "Log file"
            body = "Logger"
            msg.attach(MIMEText(body, 'plain'))
            filename = "log.log"
            attachment = open(r"C:\Arb\log.log", "rb")
            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename=%s" % filename)
            msg.attach(p)
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(fromaddr, "Hexadecimalqwertyuiop")
            text = msg.as_string()
            s.sendmail(fromaddr, toaddr, text)
            print("Mail Sent!")
            c = False
        except Exception:
            time.sleep(5)
            print("No Internet please try Again!")
            c = True

    s.quit()
x = datetime.datetime.now()

cur = x.strftime("%x")
curr = str(cur)

alphabet = string.ascii_letters + string.digits
ran1 = ''.join(secrets.choice(alphabet) for i in range(9))
f = ''.join(random.sample(string.ascii_lowercase, 9))
def prnt():
    print("""                      

                                     1.encrypt the text
                                     2.Decrypt the text



                                                                                           """)
def bar():
    progress = progressbar.ProgressBar()
    for i in progress(range(12)):
        time.sleep(0.1)
k = ''
import os
import sys
import time
print("Just For Security Purpose Answer a Question")
print("\n\n")
n=str(random.randrange(0, 50000))
timestamp1 = time.time()
def OTP():
    toaddr = input("Your E-mail:")
    fromaddr = "cyberbot1502@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "OTP"
    body = n+"\nThis OTP is valid for only 20Seconds"
    msg.attach(MIMEText(body, 'plain'))
    p = MIMEBase('application', 'octet-stream')
    text = msg.as_string()
    c = True
    while c:
        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.ehlo()
            s.starttls()
            s.login(fromaddr, "Hexadecimalqwertyuiop")
            s.sendmail(fromaddr, toaddr, text)
            c = False
        except Exception:
            time.sleep(5)
            print("No Internet please try Again!")
            c = True
    s.quit()
OTP()
x=getpass.getpass("OTP>")
timestamp2 = time.time()
if x==n:
    print("OTP Verified!")
    count=0
    if (timestamp2-timestamp1)<20:
        print("Login Successful!")
        print(timestamp2-timestamp1)
        os.system('cls')
        count = 1
    else:
        print(Fore.LIGHTBLUE_EX+"Time Out,Login Again!")
        print(Style.RESET_ALL)
        count=0
else:
    print(Fore.GREEN+"Invalid OTP!")
    print(Style.RESET_ALL)
    count=0

def bashenc():
    q = open(r"C:\Arb\log.log", "a")
    logging.basicConfig(filename='C:\Arb\log.log', level=logging.DEBUG)
    logging.debug('Start of the Bash Encryption')
    q.write(' ')
    q.write("\n")
    q.close()

    s = input("Enter the message to Encrypt:")
    s1 = ""
    for k in s:
        j = ord(k)
        if 65 <= ord(k) <= 90 or 97 <= ord(k) <= 122:
            s1 += (chr(90 - (ord(k) - 65))) if k.isupper() else chr(122 - (ord(k) - 97))

        elif j >= 48 and j <= 57:
            # print(chr(j), end="")
            s1 += chr(j)


        elif j >= 33 and j <= 47:
            s1 += chr(j)


        elif j >= 58 and j <= 64:
            # print(chr(j), end="")
            s1 += chr(j)


        elif j >= 91 and j <= 96:
            # print(chr(j), end="")
            s1 += chr(j)

        elif j >= 123 and j <= 126:
            # print(chr(j), end="")
            s1 += chr(j)


        else:
            s1 += k

    print(Fore.CYAN + "Encrypted message is:")
    print(s1)
    print(Style.RESET_ALL)
    q = open(r"C:\Arb\log.log", "a")
    logging.basicConfig(filename='C:\Arb\log.log', level=logging.DEBUG)
    logging.debug('END of the Bash Encryption')
    q.write(' ')
    q.write("\n")
    q.close()
def bashdec():
    q = open(r"C:\Arb\log.log", "a")
    logging.basicConfig(filename='C:\Arb\log.log', level=logging.DEBUG)
    logging.debug('Start of the Bash Decryption')
    q.write(' ')
    q.write("\n")
    q.close()
    s = input("Enter the message to Decrypt:")
    s1 = ""
    for k in s:
        j = ord(k)
        if 65 <= ord(k) <= 90 or 97 <= ord(k) <= 122:
            s1 += (chr(90 - (ord(k) - 65))) if k.isupper() else chr(122 - (ord(k) - 97))

        elif j >= 48 and j <= 57:
            s1 += chr(j)


        elif j >= 33 and j <= 47:
            s1 += chr(j)


        elif j >= 58 and j <= 64:
            s1 += chr(j)


        elif j >= 91 and j <= 96:
            s1 += chr(j)


        elif j >= 123 and j <= 126:
            s1 += chr(j)


        else:
            s1 += k

    print(Fore.CYAN + "Decrypted message is:", s1)
    print(Style.RESET_ALL)
    q = open(r"C:\Arb\log.log", "a")
    logging.basicConfig(filename='C:\Arb\log.log', level=logging.DEBUG)
    logging.debug('End of the Bash Encryption')
    q.write(' ')
    q.write("\n")
    q.close()
def rotenc():
    q = open(r"C:\Arb\log.log", "a")
    logging.basicConfig(filename='C:\Arb\log.log', level=logging.DEBUG)
    logging.debug('Start of the ROT13 Encryption')
    q.write(' ')
    q.write("\n")
    q.close()
    s = ""
    j = None
    s = input("Enter ur string here to encrypt:")
    li = len(s)
    print(Fore.CYAN + "Encrypted message is:", end="")
    print(Style.RESET_ALL)
    time.sleep(4)
    while li != 0:
        for i in s:
            j = ord(i)
            if j >= 97 and j <= 109 or j >= 65 and j <= 77:
                j = j + 13
                print(chr(j), end="")
                li = li - 1

            elif j >= 110 and j <= 122 or j >= 78 and j <= 90:
                j = j - 13
                print(chr(j), end="")
                li = li - 1

            elif j == 32:
                print(chr(j), end="")
                li = li - 1

            elif j >= 48 and j <= 57:
                print(chr(j), end="")
                li = li - 1

            elif j >= 33 and j <= 47:
                print(chr(j), end="")
                li = li - 1

            elif j >= 58 and j <= 64:
                print(chr(j), end="")
                li = li - 1

            elif j >= 91 and j <= 96:
                print(chr(j), end="")
                li = li - 1

            elif j >= 123 and j <= 126:
                print(chr(j), end="")
                li = li - 1

    q = open(r"C:\Arb\log.log", "a")
    logging.basicConfig(filename='C:\Arb\log.log', level=logging.DEBUG)
    logging.debug('End of the ROT13 Encryption')
    q.write(' ')
    q.write("\n")
    q.close()
def rotdec():
    q = open(r"C:\Arb\log.log", "a")
    logging.basicConfig(filename='C:\Arb\log.log', level=logging.DEBUG)
    logging.debug('Start of the ROT13 Decryption')
    q.write(' ')
    q.write("\n")
    q.close()
    s = ""
    s = input("Enter the encrypted string to decrypt it:")
    li = len(s)
    print(Fore.CYAN + "Decrypted message is:", end="")
    print(Style.RESET_ALL)
    time.sleep(4)
    while li != 0:
        for i in s:
            j = ord(i)
            if j >= 97 and j <= 109 or j >= 65 and j <= 77:
                j = j + 13
                print(chr(j), end="")
                li = li - 1

            elif j >= 110 and j <= 122 or j >= 78 and j <= 90:
                j = j - 13
                print(chr(j), end="")
                li = li - 1

            elif j == 32:
                print(chr(j), end="")
                li = li - 1

            elif j >= 48 and j <= 57:
                print(chr(j), end="")
                li = li - 1

            elif j >= 33 and j <= 47:
                print(chr(j), end="")
                li = li - 1

            elif j >= 58 and j <= 64:
                print(chr(j), end="")
                li = li - 1

            elif j >= 91 and j <= 96:
                print(chr(j), end="")
                li = li - 1

            elif j >= 123 and j <= 126:
                print(chr(j), end="")
                li = li - 1

    q = open(r"C:\Arb\log.log", "a")
    logging.basicConfig(filename='C:\Arb\log.log', level=logging.DEBUG)
    logging.debug('End of the ROT13 Decryption')
    q.write(' ')
    q.write("\n")
    q.close()
def rot22enc():
    q = open(r"C:\Arb\log.log", "a")
    logging.basicConfig(filename='C:\Arb\log.log', level=logging.DEBUG)
    logging.debug('Start of the ROT22 Encryption')
    q.write(' ')
    q.write("\n")
    q.close()
    s = ""
    j = None
    s = input("Enter ur string here to encrypt:")
    li = len(s)
    print(Fore.CYAN + "Encrypted message is:", end="")
    print(Style.RESET_ALL)
    print("\n")
    time.sleep(4)
    while li != 0:
        for i in s:
            j = ord(i)
            if j >= 97 and j <= 100 or j >= 65 and j <= 68:
                j = j + 22
                print(chr(j), end="")
                li = li - 1

            elif j >= 101 and j <= 122 or j >= 69 and j <= 90:
                j = j - 4
                print(chr(j), end="")
                li = li - 1

            elif j == 32:
                print(" ", end="")
                li = li - 1

            elif j >= 48 and j <= 57:
                print(chr(j), end="")
                li = li - 1

            elif j >= 33 and j <= 47:
                print(chr(j), end="")
                li = li - 1

            elif j >= 58 and j <= 64:
                print(chr(j), end="")
                li = li - 1

            elif j >= 91 and j <= 96:
                print(chr(j), end="")
                li = li - 1

            elif j >= 123 and j <= 126:
                print(chr(j), end="")
                li = li - 1

    q = open(r"C:\Arb\log.log", "a")
    logging.basicConfig(filename='C:\Arb\log.log', level=logging.DEBUG)
    logging.debug('End of the ROT22 Encryption')
    q.write(' ')
    q.write("\n")
    q.close()
def rot22dec():
    q = open(r"C:\Arb\log.log", "a")
    logging.basicConfig(filename='C:\Arb\log.log', level=logging.DEBUG)
    logging.debug('Start of the ROT22 Decryption')
    q.write(' ')
    q.write("\n")
    q.close()
    s = ""
    s = input("Enter the encrypted string to decrypt it:")
    li = len(s)
    print("\n", Fore.CYAN + "Decrypted message is:", end="")
    print(Style.RESET_ALL)
    print("\n")
    time.sleep(4)
    while li != 0:
        for i in s:
            j = ord(i)
            if j >= 119 and j <= 122 or j >= 87 and j <= 90:
                j = j - 22
                print(chr(j), end="")
                li = li - 1

            elif j >= 97 and j <= 118 or j >= 65 and j <= 86:
                j = j + 4
                print(chr(j), end="")
                li = li - 1

            elif j == 32:
                print(" ", end="")
                li = li - 1

            elif j >= 48 and j <= 57:
                print(chr(j), end="")
                li = li - 1

            elif j >= 33 and j <= 47:
                print(chr(j), end="")
                li = li - 1

            elif j >= 58 and j <= 64:
                print(chr(j), end="")
                li = li - 1

            elif j >= 91 and j <= 96:
                print(chr(j), end="")
                li = li - 1

            elif j >= 123 and j <= 126:
                print(chr(j), end="")
                li = li - 1

    q = open(r"C:\Arb\log.log", "a")
    logging.basicConfig(filename='C:\Arb\log.log', level=logging.DEBUG)
    logging.debug('End of the ROT22 Decryption')
    q.write(' ')
    q.write("\n")
    q.close()
def simenc():
    q = open(r"C:\Arb\log.log", "a")
    logging.basicConfig(filename='C:\Arb\log.log', level=logging.DEBUG)
    logging.debug('Start of the Simple Encryption')
    q.write(' ')
    q.write("\n")
    q.close()
    s = ""
    s = input("Enter the string to encrypt here:")
    li = len(s)
    print(Fore.CYAN + "Encrypted message is:", end="")
    print(Style.RESET_ALL)
    print("\n")
    for i in s:
        j = ord(i)
        if j == 32:
            print(chr(j), end="")
            li = li - 1

        elif j >= 48 and j <= 57:
            print(chr(j), end="")
            li = li - 1

        elif j >= 33 and j <= 47:
            print(chr(j), end="")
            li = li - 1

        elif j >= 58 and j <= 64:
            print(chr(j), end="")
            li = li - 1

        elif j >= 91 and j <= 96:
            print(chr(j), end="")
            li = li - 1

        elif j >= 123 and j <= 126:
            print(chr(j), end="")
            li = li - 1

        else:
            j = j + 1
            print(chr(j), end="")
            li = li - 1
    q = open(r"C:\Arb\log.log", "a")
    logging.basicConfig(filename='C:\Arb\log.log', level=logging.DEBUG)
    logging.debug('End of the Simple Encryption')
    q.write(' ')
    q.write("\n")
    q.close()
def simdec():
    q = open(r"C:\Arb\log.log", "a")
    logging.basicConfig(filename='C:\Arb\log.log', level=logging.DEBUG)
    logging.debug('Start of the Simple Dencryption')
    q.write(' ')
    q.write("\n")
    q.close()
    s = ""
    s = input("Enter the encrypted string here to decrypt it:")
    li = len(s)
    print(Fore.CYAN + "Decrypted message is:", end="")
    print(Style.RESET_ALL)
    print("\n")
    for i in s:
        j = ord(i)
        if j == 32:
            print(chr(j), end="")
            li = li - 1

        elif j >= 48 and j <= 57:
            print(chr(j), end="")
            li = li - 1

        elif j >= 33 and j <= 47:
            print(chr(j), end="")
            li = li - 1

        elif j >= 58 and j <= 64:
            print(chr(j), end="")
            li = li - 1

        elif j >= 91 and j <= 96:
            print(chr(j), end="")
            li = li - 1

        elif j >= 123 and j <= 126:
            print(chr(j), end="")
            li = li - 1

        else:
            j = j - 1
            print(chr(j), end="")
            li = li - 1
    q = open(r"C:\Arb\log.log", "a")
    logging.basicConfig(filename='C:\Arb\log.log', level=logging.DEBUG)
    logging.debug('End of the Simple Decryption')
    q.write(' ')
    q.write("\n")
    q.close()
def cenc():
    q = open(r"C:\Arb\log.log", "a")
    logging.basicConfig(filename='C:\Arb\log.log', level=logging.DEBUG)
    logging.debug('Start of the Ceaser-Keyed Encryption')
    q.write(' ')
    q.write("\n")
    q.close()
    s = "abcdefghijklmnopqrstuvwxyz"
    print("Current working string is:", s)
    k = input("Input a single word key u want to use for encryption:")
    if len(k) > 1:
        print("App Crashed!Sending report to the developer!")
        g = open(r"C:\Arb\log.log", "a")
        logging.basicConfig(filename='C:\Arb\log.log', level=logging.DEBUG)
        logging.warning('App crashed at Ceaser-Keyed Encryption')
        g.write("\n")
        mail()
        time.sleep(5)
        sys.exit(0)

    i = ord(k)
    s = s.replace(k, '')
    s = k + s
    print("Now string is:", s)
    t = input("Enter the string to Encrypt here:")
    li = len(t)
    print(Fore.CYAN + "Encrypted message is:", end="")
    print(Style.RESET_ALL)
    while li != 0:
        for n in t:
            j = ord(n)
            if j == ord('a'):
                j = i
                print(chr(j), end="")
                li = li - 1

            elif n > 'a' and n <= k:
                j = j - 1
                print(chr(j), end="")
                li = li - 1

            elif n > k:
                print(n, end="")
                li = li - 1

            elif ord(n) == 32:
                print(chr(32), end="")
                li = li - 1

            elif j >= 48 and j <= 57:
                print(chr(j), end="")
                li = li - 1

            elif j >= 33 and j <= 47:
                print(chr(j), end="")
                li = li - 1

            elif j >= 58 and j <= 64:
                print(chr(j), end="")
                li = li - 1

            elif j >= 91 and j <= 96:
                print(chr(j), end="")
                li = li - 1

            elif j >= 123 and j <= 126:
                print(chr(j), end="")
                li = li - 1

    q = open(r"C:\Arb\log.log", "a")
    logging.basicConfig(filename='C:\Arb\log.log', level=logging.DEBUG)
    logging.debug('End of the Ceaser-Keyed Encryption')
    q.write(' ')
    q.write("\n")
    q.close()
def cdec():
    q = open(r"C:\Arb\log.log", "a")
    logging.basicConfig(filename='C:\Arb\log.log', level=logging.DEBUG)
    logging.debug('Start of the Ceaser-Keyed Decryption')
    q.write(' ')
    q.write("\n")
    q.close()
    h = ""
    c = ''
    s = "abcdefghijklmonpqrstuvwxyz"
    t = input("Enter the Encrypted String to Decrypt it here:")
    k = input("Enter the key you used earlier during encryption:")
    if len(k) > 1:
        print("App Crashed!Sending report to the developer!")
        g = open(r"C:\Arb\log.log", "a")
        logging.basicConfig(filename='C:\Arb\log.log', level=logging.DEBUG)
        logging.debug('App Crashed at Ceaser-Keyed Decryption')
        g.write("\n")
        mail()
        time.sleep(5)
        sys.exit(0)

    s = s.replace(k, '')
    s = k + s
    i = ord(k)
    li = len(t)
    print(Fore.CYAN + "Decrypted message is:", end="")
    print(Style.RESET_ALL)
    for j in t:
        p = ord(j)
        if j > k:
            print(j, end="")

        elif j < k:
            if j == ' ':
                print(' ', end="")

            else:
                if p >= 48 and p <= 57:
                    print(chr(p), end="")
                    li = li - 1

                elif p >= 33 and p <= 47:
                    print(chr(p), end="")
                    li = li - 1

                elif p >= 58 and p <= 64:
                    print(chr(p), end="")
                    li = li - 1

                elif p >= 91 and p <= 96:
                    print(chr(p), end="")
                    li = li - 1

                elif p >= 123 and p <= 126:
                    print(chr(p), end="")
                    li = li - 1

                else:
                    j = chr(ord(j) + 1)
                    print(j, end="")

        elif j == k:
            print('a', end="")

    q = open(r"C:\Arb\log.log", "a")
    logging.basicConfig(filename='C:\Arb\log.log', level=logging.DEBUG)
    logging.debug('End of the Ceaser-Keyed Decryption')
    q.write(' ')
    q.write("\n")
    q.close()
def delay_print(s):
    for c in s:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(0.1)
os.system("cls")
auth()

if count == 1:
    # os.system(r"C:\Arb\cartoon.exe")
    choice = None
    p()
    delay_print("This Script Can Encrypt Ur Message In a Different Manner So That No Third Person Can Read It!")
    print("\n\n\n")
    choice = int(input("\nEnter 1 to start encryption and decryption process and 0 to exit the program:"))
    if choice == 0:
        delay_print("Thanks for using me!")
        mail()
        time.sleep(3)
        sys.exit(0)

    bar()

    while choice != 0:
        print("""

                   1.Atbash Encryption
                   2.Rot13
                   3.Rot22
                   4.Simple Encryption(add 1)
                   5.caesar(with ur key for only small alphabets)
                   6.Send Feedback to the Developer
                   7.Exit The program 

                                               """)

        c = 0
        ch = None
        c = int(input("Please Choose ur encryption Method from the following techniques listed above:"))
        if c == 6:
            fromaddr = "cyberbot1502@gmail.com"
            toaddr = "cyberbot1502@gmail.com"
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            sub = input("Subject of Mail:")
            bod = input("Body of the mail!:")
            msg['Subject'] = sub
            body = bod
            msg.attach(MIMEText(body, 'plain'))
            p = MIMEBase('application', 'octet-stream')
            text = msg.as_string()
            c = True
            while c:
                try:
                    s = smtplib.SMTP('smtp.gmail.com', 587)
                    s.ehlo()
                    s.starttls()
                    s.login(fromaddr, "Hexadecimalqwertyuiop")
                    s.sendmail(fromaddr, toaddr, text)
                    c = False
                    print("Mail Sent!")
                except Exception:
                    time.sleep(5)
                    print("No Internet please try Again!")
                    c = True

            s.quit()

        if c == 7:
            FILE_ATTRIBUTE_HIDDEN = 0x1

            # rett = ctypes.windll.kernel32.SetFileAttributesW(r'C:\log.log',
            # FILE_ATTRIBUTE_HIDDEN)
            delay_print("Thanks for using me!")
            mail()
            sys.exit()

        if c == 1:
            while ch != 0:
                prnt()
                f = int(input("Enter ur choice what to do now:"))
                if f == 1:
                    bashenc()
                if f == 2:
                    bashdec()
                ch = int(input("\nWant to do some more encryption-decryption task on Atbash then enter 2 otherwise 0:"))

        elif c == 2:
            hc = None
            while hc != 0:
                prnt()
                f = int(input("Enter ur choice what to do now:"))
                if f == 1:
                    rotenc()
                if f == 2:
                    rotdec()

                hc = int(input("\nTo do some more task in ROT13 enter 4 otherwise 0:"))
                print("\n")

        elif c == 3:
            cc = None
            while cc != 0:
                prnt()
                f = int(input("Enter ur choice what to do now:"))
                if f == 1:
                    rot22enc()
                if f == 2:
                    rot22dec()

                cc = int(input("\nTo do more task in ROT22 enter 4 otherwise 0:"))
                print("\n")

        elif c == 4:
            g = None
            while g != 0:
                prnt()
                f = int(input("Enter ur choice what to do now:"))
                if f == 1:
                    simenc()

                if f == 2:
                    simdec()

                g = int(input("\nTo do more task in Simple method enter 5 otherwise 0:"))

        elif c == 5:
            i = None
            while i != 0:
                prnt()
                g = int(input("Enter ur choice what to do now:"))
                if g == 1:
                    cenc()
                if g == 2:
                    cdec()

                i = int(input("\nTo do more task in caesor keyed enter 6 otherwise 0:"))


else:
    print(Fore.RED + "Wrong OTP!")
    print(Style.RESET_ALL)

    time.sleep(4)
