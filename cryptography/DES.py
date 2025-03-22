from Crypto.Cipher import DES
# from Crypto.Random import get_random_bytes

def encrypt(message,key) :
    key=key.encode()

    # key = get_random_bytes(8)
    def pad(text):
        while len(text) % 8 != 0 :
            text += b' '
        return text

    des=DES.new(key,DES.MODE_ECB)
    text=pad(message.encode())
    encrypted=des.encrypt(text)
    return encrypted

def decrypt(message,key) :
    key=key.encode()
    message=message.encode('latin1')
    print(message)
    des=DES.new(key,DES.MODE_ECB)
    decrypted=des.decrypt(message).rstrip()
    return decrypted.decode()

# print(encrypt('hello i am iqbal','12345678'))
# print(decrypt('\x97Q\x8f\xd0\x8b\xe9\xdc\x932e\x8dE\xed\xca\x11\x84','iqbalahm'))
#
# # b'V\xa1\xabB\xeb\xc35E\xab#+\xd7\x17\xd8\xd8='
# # b'yi\xca3\xdd\x94I:\x17\xb7\xa3Fax\xc6\x82'

# a=bytes(range(256))
# a='{£"ÓSìHÙÂ¶øÖ'
# # b= a.decode('latin1')
# c=a.encode('latin1')
# print(c)

# from tkinter import *
# root = Tk()
# global login_success_screen
# login_success_screen = Toplevel(login_screen)
# login_success_screen.title("Login Success")
# login_success_screen.geometry("300x200")
# Label(login_success_screen, text="Select your Encryption Method").pack()
# menu_btn = Menubutton(root, text='Select', relief=RAISED)
# menu_btn.grid(rowspan=10, columnspan=10)
# root.geometry('400x400')
# menu_btn.menu = Menu(menu_btn, tearoff=0)
# menu_btn["menu"] = menu_btn.menu
# Ceaser = IntVar()
# DES = IntVar()
# AES = IntVar()
# Sig = IntVar()
# RSA = IntVar()
# Elgamal = IntVar()
#
# menu_btn.menu.add_checkbutton(label="Ceaser", variable=Ceaser, command=lambda: self.text_area(root, "Ceaser"))
# menu_btn.menu.add_checkbutton(label="DES", variable=DES, command=lambda: self.text_area(root, "DES"))
# menu_btn.menu.add_checkbutton(label="AES", variable=AES, command=lambda: self.text_area(root, "AES"))
# menu_btn.menu.add_checkbutton(label="Sig", variable=Sig, command=lambda: self.text_area(root, "Sig"))
# menu_btn.menu.add_checkbutton(label="RSA", variable=RSA, command=lambda: self.text_area(root, "RSA"))
# menu_btn.menu.add_checkbutton(label="Elgamal", variable=Elgamal, command=lambda: self.text_area(root, "Elgamal"))
# menu_btn.pack(padx=20, pady=20)
# root.mainloop()
