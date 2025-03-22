from tkinter import *
from tkinter import messagebox
import sqlite3
import hashlib

def login():

    def sign_up():
        def signup():
            username = user.get()
            password = code.get()
            confirm_code = confirm_password.get()
            conn = sqlite3.connect('database.db')
            cur = conn.cursor()

            cur.execute("""
                    CREATE TABLE IF NOT EXISTS database(
                        id INTEGER PRIMARY KEY,
                        username VARCHAR(255) NOT NULL,
                        password VARCHAR(255) NOT NULL
                    )
                    """)
            username1, password1 = username, hashlib.sha256(password.encode()).hexdigest()
            cur.execute('INSERT INTO database (username, password) VALUES(?,?)', (username1, password1))
            conn.commit()
            messagebox.showinfo('Signup', 'successfully sign up')

        screen = Toplevel(root)
        screen.geometry('925x500+100+100')
        screen.resizable(False, False)
        screen.title('login')
        screen.config(bg='white')

        img = PhotoImage(file='sign_up.png')
        Label(screen, image=img, bg='white').place(x=50, y=90)

        frame = Frame(screen, width=350, height=360, bg='white')
        frame.place(x=480, y=50)
        heading = Label(frame, text='Sign up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=100, y=5)

        def on_enter(e):
            name = user.get()
            if name == 'Username':
                user.delete(0, 'end')
                user.config(fg='black')

        def on_leave(e):
            name = user.get()
            if name == '':
                user.insert(0, 'Username')
                user.config(fg='gray')

        user = Entry(frame, width=25, fg='gray', bg='white', borderwidth=0, font=('Microsoft YaHei UI Light', 11))
        user.place(x=30, y=80)
        user.insert(0, 'Username')
        user.bind('<FocusIn>', on_enter)
        user.bind('<FocusOut>', on_leave)
        Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

        def on_enter(e):
            password = code.get()
            if password == 'Password':
                code.delete(0, 'end')
                code.config(fg='black',show='*')

        def on_leave(e):
            name = code.get()
            if name == '':
                code.insert(0, 'Password')
                code.config(fg='gray', show='')

        code = Entry(frame, width=25, fg='gray', bg='white', borderwidth=0, font=('Microsoft YaHei UI Light', 11))
        code.place(x=30, y=150)
        code.insert(0, 'Password')
        code.bind('<FocusIn>', on_enter)
        code.bind('<FocusOut>', on_leave)
        Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

        def on_enter(e):
            confirm_code = confirm_password.get()
            if confirm_code == 'confirm Password':
                confirm_password.delete(0, 'end')
                confirm_password.config(fg='black',show='*')

        def on_leave(e):
            name = confirm_password.get()
            if name == '':
                confirm_password.insert(0, 'Password')
                confirm_password.config(fg='gray', show='')

        confirm_password = Entry(frame, width=25, fg='gray', bg='white', borderwidth=0,
                                 font=('Microsoft YaHei UI Light', 11))
        confirm_password.place(x=30, y=220)
        confirm_password.insert(0, 'confirm Password')
        confirm_password.bind('<FocusIn>', on_enter)
        confirm_password.bind('<FocusOut>', on_leave)
        Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

        Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', borderwidth=0, command=signup).place(x=35,y=280)

        label = Label(frame, text="I have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
        label.place(x=75, y=340)

        def signin():
            screen.destroy()
        sign_in = Button(frame, width=6, text='Sign in', borderwidth=0, bg='white', fg='#57a1f8', cursor='hand2', command=signin)
        sign_in.place(x=200, y=340)
        root.mainloop()

    def signin():
        username=user.get()
        password=code.get()
        password1=hashlib.sha256(password.encode()).hexdigest()
        print(username)
        print(password1)
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM database WHERE username = ? AND password = ?",(username,password1))

        ###############################################################################################
        if cur.fetchall():
            import algorithm

        elif username!= 'admin' and code!= 'admin' :
            messagebox.showerror('Invalid', 'Invalid Username and Password')
    root=Tk()
    root.geometry('925x500+100+100')
    root.resizable(False,False)
    root.title('login')
    root.config(bg='white')

    img=PhotoImage(file='login.png')
    Label(root, image=img, bg='white').place(x=50, y=50)

    frame=Frame(root, width=350, height=350, bg= 'white')
    frame.place(x=480, y=70)
    heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    def on_enter(e):
        if user.get() == 'Username':
            user.delete(0,'end')
            user.config(fg='black')
    def on_leave(e):
        if user.get() == '' :
            user.insert(0,'Username')
            user.config(fg='gray')
    user=Entry(frame, width=25, fg='gray', bg='white', borderwidth=0,  font=('Microsoft YaHei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='black').place(x=25,y=107)

    def on_enter(e):
        if code.get() == 'Password':
            code.delete(0,'end')
            code.config(fg='black', show='*',font='bold')

    def on_leave(e):
        if code.get() == '' :
            code.insert(0,'Password')
            code.config(fg='gray',show='')

    code = Entry(frame, width=25, fg='gray', bg='white', borderwidth=0, font=('Microsoft YaHei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0, 'Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', borderwidth=0, command=signin ).place(x=35, y=204)

    label=Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
    label.place(x=75, y=270)

    sign_up= Button(frame, width=6, text='Sign up', borderwidth=0, bg='white', fg='#57a1f8', cursor='hand2', command=sign_up)
    sign_up.place(x=215, y=270)
    root.mainloop()

if __name__ == '__main__' :
    login()