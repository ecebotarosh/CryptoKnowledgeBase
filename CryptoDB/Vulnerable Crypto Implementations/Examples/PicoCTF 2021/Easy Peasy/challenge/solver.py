#!/usr/bin/env python3
from pwn import *
from binascii import unhexlify
context.log_level = "error"

r = remote("mercury.picoctf.net", 20266)
r.recvuntil("flag!\n")
enc_flag = unhexlify(r.recvline().strip())
r.recv()
#We force the algorithm to wrap around himself and get back to using the key from position 0
r.sendline((50000-len(enc_flag))*"A")
r.recvuntil("? ")
#Now we leak the xored key, that was used to encrypt the flag from the start
r.sendline(len(enc_flag)*"A")
r.recvline()
hex_xored_key = r.recvline()
r.recvline()

xored_key = unhexlify(hex_xored_key.strip())
key = xor(xored_key, len(enc_flag)*"A")
flag = xor(enc_flag, key)
print("picoCTF{" + flag.decode('utf-8') + "}")
