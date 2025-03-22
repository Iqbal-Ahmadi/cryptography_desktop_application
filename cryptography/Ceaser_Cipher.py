import base64

def encrypt(message):
    encode_msg = message.encode('ascii')
    base64_bytes = base64.b64encode(encode_msg)
    encrypted = base64_bytes.decode('ascii')
    return encrypted

def decrypt(message) :
    decode_msg = message.encode('ascii')
    base64_bytes = base64.b64decode(decode_msg)
    decrypted = base64_bytes.decode('ascii')
    return decrypted

# if __name__ == '__main__':
#     print(encrypt('hello my name is iqbal'))
#     print(decrypt('aGVsbG8gbXkgbmFtZSBpcyBpcWJhbA=='))

# import ast
# import codecs
# a=b'\xe2\xa8\xfb@<\xa9\x06\xae'
# # bytes1=ast.literal_eval(a)
# # print(bytes1.decode('utf-8'))
# b=codecs.decode(a,'cp1250')
# # b=a.decode('utf-8').rstrip('\x00')
# # c=b.encode()
# # print(a.('latin1'))
# # print(b)
# uni=str(a)
# uni=a.decode('ascii')
# print(uni)