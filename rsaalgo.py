# from email import message
# from inspect import signature
import rsa

def generate_keys():
    (pubKey, privKey) = rsa.newkeys(500)
    with open('keys/pubKey.pem','wb') as f:
        f.write(pubKey.save_pkcs1('PEM'))

    with open('keys/privKey.pem','wb') as f:
        f.write(privKey.save_pkcs1('PEM'))

def load_keys():
    with open('keys/pubKey.pem','rb') as f:
        pubKey = rsa.PublicKey.load_pkcs1(f.read())

    with open('keys/privKey.pem','rb') as f:
        privKey = rsa.PrivateKey.load_pkcs1(f.read())
    
    return pubKey,privKey

def encrypt(msg,key):
    return rsa.encrypt(msg.encode(),key)

def decrypt(ciphertext,key):
    try:
        return rsa.decrypt(ciphertext,key).decode()
    except:
        return False

generate_keys()
pubKey, privKey = load_keys()
