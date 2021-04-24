#!/usr/bin/env python3
from Crypto.Util.number import inverse, long_to_bytes
from factordb.factordb import FactorDB

c = 240986837130071017759137533082982207147971245672412893755780400885108149004760496
n = 831416828080417866340504968188990032810316193533653516022175784399720141076262857
e = 65537

f = FactorDB(n)
f.connect()
p, q = f.get_factor_list()

phi = (p-1)*(q-1)
d = inverse(e, phi)
m = pow(c, d, n)
print(long_to_bytes(m).decode('utf-8'))
