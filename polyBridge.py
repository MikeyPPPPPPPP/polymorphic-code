
from cryptography.fernet import Fernet

def code(file):
	with open(file) as x:
		return x.read()

#the code we want to execute
code = code(__file__)


key = Fernet.generate_key()

encoded_message = code.encode()
f = Fernet(key)
encrypted_message = f.encrypt(encoded_message)

poly = """
encrypted_message = '"""+encrypted_message.decode()+"""'
key = """+str(key)+"""
from cryptography.fernet import Fernet
f = Fernet(key)
decrypted_message = f.decrypt(encrypted_message.encode())
exec(decrypted_message.decode())
"""
print(poly)


import random
test = open(str(random.randint(1,9))+'.py','w')
test.write(poly)

import os
os.remove(__file__)

