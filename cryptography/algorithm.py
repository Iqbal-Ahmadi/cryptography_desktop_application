import random
from tkinter import *
from tkinter import messagebox
import Ceaser_Cipher
import DES
import AES
import RSA
import Elgamal_encryption
import digital_signature
import secrets



def encryption():
    checkbutton=checkbutton_var.get()
    options= option_var.get()
    message = plain_text.get(1.0,'end')
    key1=key.get()

    if options == 'Ceaser Cipher' :
        cipher_text.delete(1.0,END)
        cipher_text.insert(END,Ceaser_Cipher.encrypt(message))

    elif options == 'DES' :
        cipher_text.delete(1.0, END)
        message = message.rstrip()
        if checkbutton == 1 :
            key1=secrets.token_hex(4)
            key_entry.delete(0,'end')
            key_entry.insert(END,key1)
        elif key1 == '':
            messagebox.showerror('Invalid','input you key')
        elif len(key1) != 8 :
            messagebox.showerror('Invalid', 'key length must be 8 character')
        cipher_text.insert(END,DES.encrypt(message,key1))

    elif options == 'AES':
        cipher_text.delete(1.0, END)
        if checkbutton == 1 :
            key1 = secrets.token_hex(8)
            key_entry.delete(0, 'end')
            key_entry.insert(END, key1)
        elif key1 == '':
            messagebox.showerror('Invalid', 'input you key')
        elif len(key1) != 16:
            messagebox.showerror('Invalid', 'key length must be 16 character')
        cipher_text.insert(END, AES.encrypt(message,key1))

    elif options == 'RSA' :
        cipher_text.delete(1.0,'end')
        if checkbutton == 1 :
            key1= open('public.pem', 'rb').read()
            key_entry.delete(0, END)
            key_entry.insert(END,key1)
        elif key1 == '':
            messagebox.showerror('Invalid', 'input you key')

        cipher=RSA.encrypt(key1,message)
        h=cipher.hex()
        cipher_text.insert(END, h)

    elif options == 'Digital signature' :
        cipher_text.delete(1.0, 'end')
        if checkbutton == 1 :
            key1 = open('private.pem','rb').read()
            key_entry.delete(0, 'end')
            key_entry.insert(END, key1)
        elif key1 == '':
            messagebox.showerror('Invalid', 'input you key')

        cipher = digital_signature.signature(message, key1)
        h = cipher.hex()
        cipher_text.insert(END, h)

    elif options == 'Elgamal' :
        global q
        global h1
        global g
        global p
        global ciphered
        global k
        cipher_text.delete(1.0, 'end')
        if checkbutton == 1 :
            q = random.randint(pow(10, 20), pow(10, 50))
            k = Elgamal_encryption.gen_key(q)
            key_entry.delete(0, 'end')
            key_entry.insert(END, k)
            g = random.randint(2, q)
            h1 = Elgamal_encryption.power(g, k, q)
            ciphered, p = Elgamal_encryption.encrypt(message, q, h1, g)
            cipher_text.insert(END, ciphered)
        elif key1 == '':
            messagebox.showerror('Invalid', 'input you key')
    if key_entry.get()!= 'Enter your key' :
        key_entry.config(fg='black')
    checkbutton_var.set(0)

def decryption():
    options = option_var.get()
    message = plain_text.get(1.0, 'end')
    key1 = key.get()
    checkbutton=checkbutton_var.get()

    if options == 'Ceaser Cipher':
        cipher_text.delete(1.0, END)
        cipher_text.insert(END, Ceaser_Cipher.decrypt(message))

    elif options == 'DES' :
        cipher_text.delete(1.0, END)
        message = message.rstrip()
        if key1 == '':
            messagebox.showerror('Invalid','input you key')
        elif len(key1) != 8 :
            messagebox.showerror('Invalid', 'key length must be 8 character')
        cipher_text.insert(END,DES.decrypt(message,key1))

    elif options == 'AES':
        cipher_text.delete(1.0, END)
        message = message.rstrip()
        if key1 == '':
            messagebox.showerror('Invalid', 'input you key')
        elif len(key1) != 16:
            messagebox.showerror('Invalid', 'key length must be 16 character')
        cipher_text.insert(END, AES.decrypt(message,key1))

    elif options == 'RSA' :
        cipher_text.delete(1.0,'end')
        if checkbutton == 1 :
            with open('private.pem','rb') as f :
                key1 = f.read()
            key_entry.delete(0, END)
            key_entry.insert(END, key1)
        elif key1 == '':
            messagebox.showerror('Invalid', 'input you key')
        message=bytes.fromhex(message)
        cipher=RSA.decrypt(key1,message)
        print(cipher)
        # h=cipher.hex()
        cipher_text.insert(END, cipher)

    elif options == 'Digital signature' :
        cipher_text.delete(1.0, 'end')
        if key1 == '':
            messagebox.showerror('Invalid', 'input you signature key')
        key1=bytes.fromhex(key1)
        cipher = digital_signature.verify(message, key1)
        print(cipher)
        cipher_text.insert(END, cipher)

    elif options == 'Elgamal' :
        cipher_text.delete(1.0, 'end')
        if key1 == '':
            messagebox.showerror('Invalid', 'input you key')
        dr_msg = Elgamal_encryption.decrypt(ciphered, p, k, q)
        cipher_text.insert(END, ''.join(dr_msg))

    if key_entry.get()!= 'Enter your key' :
        key_entry.config(fg='black')
    checkbutton_var.set(0)

win=Tk()
win.geometry('450x560+100+100')
win.config(bg='lightblue')
Label(win, text='Select algorithm to encrypt',font=('Microsoft YaHei UI Light', 14, 'bold'),bg='lightblue').place(x=20,y=5)

def optionmenu_change(*args):
    selected=option_var.get()
    if selected == 'Ceaser Cipher' :
        key_entry.delete(0,'end')
        key_entry.config(state='disabled')
        c.config(state='disabled')
    else:
        key_entry.config(state='normal',fg='gray')
        c.config(state='normal')
        key_entry.delete(0,'end')
        key_entry.insert(0,'Enter your key')

option_var=StringVar(win)
option_var.trace('w',optionmenu_change)
key=StringVar(win)
plain_var=StringVar(win)

value_inside=['Ceaser Cipher', 'DES','AES', 'RSA', 'Digital signature', 'Elgamal']
option_var.set('select an option')
option=OptionMenu(win, option_var, *value_inside)
option.place(x=20,y=40)

def on_enter(e):
    if plain_text.get(1.0, 'end-1c') == 'Enter your text here':
        plain_text.delete(1.0,'end-1c')
        plain_text.config(fg='black')

def on_leave(e):
    if plain_text.get(1.0, 'end-1c') == '' :
        plain_text.insert(END,'Enter your text here')
        plain_text.config(fg='gray')

plain_text=Text(win, font='Arial 14',fg='gray', bg='white', relief=GROOVE, bd=0, width=30, height=8, border=2)
plain_text.place(x=20, y=75)
plain_text.insert(END, 'Enter your text here')
plain_text.bind('<FocusIn>',on_enter)
plain_text.bind('<FocusOut>',on_leave)

def on_enter(e):
    if key_entry.get() == 'Enter your key':
        key_entry.delete(0,'end')
        key_entry.config(fg='black')

def on_leave(e):
    if key_entry.get() == '' :
        key_entry.insert(END,'Enter your key')
        key_entry.config(fg='gray')

key_entry=Entry(win, textvariable=key, fg='gray', width=30, bd=0, font=('arial', 15),border=2)
key_entry.place(x=20 ,y=260)
key_entry.insert(0,'Enter your key')
key_entry.bind('<FocusIn>', on_enter)
key_entry.bind('<FocusOut>', on_leave)


checkbutton_var = IntVar(win)
c=Checkbutton(win,variable=checkbutton_var, text='generate a key', bg='lightblue')
c.place(x=20,y=290)

Button(win, width=20, height=2, text='Encrypt', bg='green', fg='white',borderwidth=0, command=encryption).place(x=20, y=320)
Button(win, width=20, height=2, text='Decrypt', bg='green', fg='white',borderwidth=0, command=decryption).place(x=180, y=320)

cipher_text=Text(win, font='Arial 14',fg='black', bg='white', relief=GROOVE, bd=0, width=30, height=8, border=2)
cipher_text.place(x=20, y=365)


win.mainloop()
