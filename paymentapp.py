# from email import message
# from rsaalgo import encrypt,pubKey

# # message = "Pranavi Chintakindi"
# # ciphertext = encrypt(message,pubKey)
# # print(ciphertext)


# card = input("Enter Card No:")
# name = input("Enter Name on Card:")
# pin = input("Enter pin:")

# cipher_card = encrypt(card,pubKey)
# cipher_name = encrypt(name,pubKey)
# cipher_pin = encrypt(pin,pubKey)

from urllib import request
from rsaalgo import encrypt,pubKey,decrypt,privKey
from flask import Flask,render_template,request
import mysql.connector


app = Flask(__name__)

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cyber"    
    )

@app.route('/')
@app.route('/register',methods=['POST','GET'])
def register():
    msg = ''
    if request.method == 'POST':
        login = request.form
        card=login['card']
        name=login['name']
        pin = login['pin']
        cursor = mydb.cursor()

        card = encrypt(card,pubKey)
        name = encrypt(name,pubKey)
        pin = encrypt(pin,pubKey)
        
        
        cursor.execute("insert into carddeets(card,name,pin) values(%s,%s,%s)",(card,name,pin))
        mydb.commit()
        msg = "Card Details Entered Successfully"
    return render_template('form.html',msg=msg) 
        


if __name__=="__main__": #to check we only run the page
    app.run(debug=True)
