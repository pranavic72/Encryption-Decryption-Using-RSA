from email import message
from rsaalgo import encrypt,pubKey

message = "Pranavi Chintakindi"
ciphertext = encrypt(message,pubKey)
print(ciphertext)
