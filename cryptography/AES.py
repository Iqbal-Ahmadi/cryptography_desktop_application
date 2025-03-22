# # from Crypto.Random import get_random_bytes
# from Crypto.Cipher import AES
#
#
# class Aes:
#     def __init__(self, message: str, key):
#         self.message = message.encode()
#         self.key = key.encode()
#
#     def encryption(self):
#         encrypted = AES.new(self.key, AES.MODE_GCM)
#         msg_encrypted = encrypted.encrypt(self.message)
#         nonce = encrypted.nonce
#         return msg_encrypted, nonce
#
#     def decryption(self):
#         self.message.decode()
#         cipherText, nonce = self.encryption()
#         msg_encrypted = AES.new(self.key, AES.MODE_GCM, nonce)
#         msg_decrypted = msg_encrypted.decrypt(cipherText)
#         return msg_decrypted.decode()


# ob = Aes('Salaam Afghanistan', 'iqbalahmadiiqbal')
# print(ob.encryption())
# # print(ob.decryption())
# print('\{°ñ¾Í:¹Î ¥ò\{ûåôé_g\"ýÏ5ß'.encode(''))

from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes

def encrypt(message,key) :
    key=key.encode()

    # key = get_random_bytes(8)
    def pad(text):
        while len(text) % 16 != 0 :
            text += b' '
        return text

    des=AES.new(key,AES.MODE_ECB)
    text=pad(message.encode())
    encrypted=des.encrypt(text)
    return encrypted

def decrypt(message,key) :
    key=key.encode()
    message=message.encode('latin1')
    print(message)
    des=AES.new(key,AES.MODE_ECB)
    decrypted=des.decrypt(message).rstrip()
    return decrypted.decode()
