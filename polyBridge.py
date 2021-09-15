from cryptography.fernet import Fernet


#the code we want to execute
code = '''

'''


#this is the encrypted code witha "randomly" genrated key so it is "diffrent" ever time it is encrypted ie Polymorphisom
key = Fernet.generate_key()

encoded_message = code.encode()
f = Fernet(key)
encrypted_message = f.encrypt(encoded_message)


#this will decrypt the data
f = Fernet(key)
decrypted_message = f.decrypt(encrypted_message)


poly = """
encrypted_message = '"""+encrypted_message.decode()+"""'
key = """+str(key)+"""
from cryptography.fernet import Fernet
f = Fernet(key)
decrypted_message = f.decrypt(encrypted_message.encode())
exec(decrypted_message.decode())
"""
print(poly)

