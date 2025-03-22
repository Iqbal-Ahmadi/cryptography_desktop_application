# from threading import *
# from time import *
#
# def display(str1):
#     l.acquire()
#     for i in str1:
#         print(i)
#     l.release()
#
# # creat a mutater to avoid from displaying both thread mixup
#
# l = Lock()
# t = Thread(target=display,args=('how are you ',))
# t1 = Thread(target=display,args=('i am fine',))
#
# t.start()
# t1.start()
#
# t.join()
# t1.join()

# def alphabet():
#     for i in range(65, 99):
#         print(chr(i))
#         sleep(1)
#
# t = Thread(target=alphabet, name='alphabet')
# t.start()
#
# for i in range(65, 99):
#     print(i)
#     sleep(1)
#
# t.join()

# class alphabet(Thread):
#     def run(self):
#         for i in range(65, 99):
#             print(chr(i))
#             sleep(1)
#
# t = alphabet()
# t.start()
#
# for i in range(65, 99):
#     print(i)
#     sleep(1)
#
# t.join()


import rsa

def signature(message,private_key):

    # messege='iqbalahmadi'
    private_key=rsa.PrivateKey.load_pkcs1(private_key)
    sign=rsa.sign(message.encode(),private_key,'SHA-512')
    return sign

def verify(message, sign) :
    with open('public.pem','rb') as f :
        public_key = rsa.PublicKey.load_pkcs1(f.read())

    try :
        verified=rsa.verify(message.encode(), sign, public_key)
    except :
        verified='Verification error:("Verification failed")'
    return verified
# with open('public.pem','rb') as f :
#     public_key = rsa.PublicKey.load_pkcs1(f.read())
#
# print(verify('iqbalahmadi',public_key))
# # print(signature(' ','kdkdjf'))
# # print(verify('iqbalahmadi',public_key,b'\xab\xc4s(\t\x10\x15\xc4d\xca\xb7r*$\xda_*\x1cU\xa7\x10\r\x93\xc7\xff\xe4\xa3\x06X;\xcb\x91\x97\x8cZOIa\x05\x8b\x04\xf6\xe0q{\xaf\xee\xfa\x15@S,\x89(\xb2\xd0\x9f\xf5[{#%Q\x91\xfe+B\x8eC\xb0\xbc\xb0\xd8\\n\x86\x00\xe2\x05)\xb2\xef\xcco\xa1C_\x01\xc6\xa4\xa1\xb2g\xd9\xa9\x8c>\xd5\x92bC3\x00\x8e\xca*\xfe\xd9\xdb\x87\x01\xcb\x1f\x1aRD\\2\xe2e\xda\x98o\xff"\xe36_'))

# with open('public.pem','rb') as f :
#     public_key = rsa.PublicKey.load_pkcs1(f.read())
# with open('private.pem','rb') as f :
#     private_key = rsa.PrivateKey.load_pkcs1(f.read())
#
# message='iqbalahmadi'
# sign=rsa.sign(message.encode(),private_key,'SHA-512')
# with open('sign', 'rb') as f :
#     signature=f.read()
# print(signature)
# print(rsa.verify(message.encode(),signature,public_key))