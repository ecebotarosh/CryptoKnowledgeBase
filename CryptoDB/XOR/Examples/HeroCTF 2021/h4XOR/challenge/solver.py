#!/usr/bin/env python3
from pwn import *
with open('attachments/flag.png.enc', 'rb') as f:
    encrypted = f.read()

#We know that the decrypted file has to be a valid PNG
#A PNG file starts with an 8 byte header
#So we can instantly have the urandom(8) bytes guessed
#WITHOUT BRUTEFORCE
#We get them by xoring the encrypted file with the magic bytes

magic_bytes = b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"

#Only the first 8 bytes are of interest for us
key = xor(encrypted, magic_bytes)[:8]

#0 to 9 inclusively
for i in range(10):
    with open(f'flag{i}.png', 'wb') as f:
        final_key = key + bytes([i])
        f.write(xor(final_key, encrypted))

#From the output there will only be one valid PNG file
