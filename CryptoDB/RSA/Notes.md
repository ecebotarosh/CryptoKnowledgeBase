# RSA Formulas
# Basic RSA:
N = p*q, p,q - coprimes 
phi = (p-1)(q-1)
d = inverse(e) mod phi
decrypted ciphertext = ciphertext ^ d mod N
[[Example]]

# Small e
If e == 3, there are 2 options:
1. If pow(m, e) < N we use m = e_th_root of c
2. If pow(m, e) >= N, we use m = eth_root of (c+kn), where k is a natural number [[RSA/Examples/PicoCTF 2021/Mini RSA/challenge/Challenge]]
__Sage__ works better for this stuff , but it might fail. That's why you use gmpy2


