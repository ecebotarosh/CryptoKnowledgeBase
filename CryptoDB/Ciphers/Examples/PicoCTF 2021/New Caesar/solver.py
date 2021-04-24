#!/usr/bin/env python3
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

def unshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABETS[t2][t1]

def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]



#We know that the key length is 1, so it's a very simple keyed caesar cipher
ALPHABETS = []
for potential_key in ALPHABET:
    enc = ""
    for i in ALPHABET:
        enc+=shift(i, potential_key)
    ALPHABETS.append(enc)


def b16_decode(enc):
    plain = ""
    for i in range(0, len(enc), 2):
        binary_high = ALPHABET.find(enc[i])
        binary_low = ALPHABET.find(enc[i+1])
        binary = (binary_high << 4) + binary_low
        plain+=chr(binary)
    return plain

enc_flag = "kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm"
for potential_key in ALPHABET:
    enc = ""
    for i in enc_flag:
        enc+=unshift(i, potential_key)
    if 'et_tu' in b16_decode(enc):
        print(f"[+] Key :{potential_key}")
        print("[+] Flag : picoCTF{" + b16_decode(enc) + "}") 
