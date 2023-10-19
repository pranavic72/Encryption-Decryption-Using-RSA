# from paymentapp import cipher_card,cipher_name,cipher_pin
# from rsaalgo import decrypt,privKey

# plain_card = decrypt(cipher_card,privKey)
# plain_name = decrypt(cipher_name,privKey)
# plain_pin = decrypt(cipher_pin,privKey)
# print("Card Details:")
# print("Card no: ",plain_card)
# print("Name on Card: ",plain_name)
# print("Pin: ",plain_pin)

import mysql.connector
from rsaalgo import decrypt,privKey
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cyber"    
    )
cursor = mydb.cursor()

id = input("enter id: ")
cursor.execute("select * from carddeets where id=2")

result=cursor.fetchone()
efname = result[2]
plaintext = decrypt(efname,privKey)
print(plaintext)