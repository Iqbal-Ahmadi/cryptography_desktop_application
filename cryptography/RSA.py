import rsa

def encrypt(public_key,message):
    # with open('public.pem','rb') as f :
    #     public_key = rsa.PublicKey.load_pkcs1(f.read())
    # with open('private.pem','rb') as f :
    #     private_key = rsa.PrivateKey.load_pkcs1(f.read())
    # public_key, private_key = rsa.newkeys(1024)
    # with open('public.pem','wb') as f :
    #     f.write(public_key.save_pkcs1('PEM'))
    # with open('private.pem','wb') as f :
    #     f.write(private_key.save_pkcs1('PEM'))

    # messege='hello iqbalahmadi is my password'
    public_key=rsa.PublicKey.load_pkcs1(public_key)
    encrypted_msg=rsa.encrypt(message.encode(), public_key)
    # with open('encrypted_message', 'wb') as f:
    #     f.write(encrypted_msg)
    return encrypted_msg

def decrypt(private_key,message):
    # encrypted_text = open('encrypted_message','rb') .read()
    private_key = rsa.PrivateKey.load_pkcs1(private_key)
    decrypt_message=rsa.decrypt(message, private_key)
    # print(decrypt_message.decode())
    return decrypt_message.decode()

# with open('public.pem', 'rb') as f:
    # public_key = rsa.PublicKey.load_pkcs1(f.read())
    # public_key= f.read()
# with open('private.pem', 'rb') as f:
#     private_key = rsa.PrivateKey.load_pkcs1(f.read())
#
# print(type(public_key))
# # print((public_key).decode())
# print(rsa.PublicKey.load_pkcs1(public_key))
