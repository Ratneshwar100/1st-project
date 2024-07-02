from tkinter import *
from tkinter import messagebox

def handle_sign_in():
    email = email_input.get()
    password=password_input.get()

    if email == 'ratneshwarmishra4@gmail.com' and password=='21003':
        messagebox.showinfo('DONE','Login succeful')
    else:
        messagebox.showerror('ERROR','something went wrong')
        
def handle_sign_in_with_facebook():
    email = email_input.get()
    password=password_input.get()
    if email == 'ratneshwarmishra4@gmail.com' and password=='21003':
        messagebox.showerror('ERROR','create facebook acount')
    else:
        messagebox.showerror('ERROR','create facebook acount')
    

root = Tk()

root.title('login form')

root.geometry('400x580')
root.configure(background='red')


text_label=Label(root,text='zomato',fg='white',bg='red',)
text_label.pack(pady=(50,10))
text_label.config(font=('Segoe UI Black',50))


email_label =Label(root,text='Email',fg='white',bg='red')
email_label.pack(pady=(20,5))
email_label.config(font=('verdan',13))


email_input = Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))


password_label=Label(root,text='Password',fg='white',bg='red')
password_label.pack(pady=(8,5))
password_label.config(font=('verdan',13))


password_input = Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))


login_btn=Button(root,text='sign in',bg='green',fg='white',width=14,height=1,command=handle_sign_in)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',14))


text_label=Label(root,text='OR',fg='white',bg='red',)
text_label.pack(pady=(2,19))
text_label.config(font=('Miedinger',9))





login_btn=Button(root,text='sign in with facebook',bg='blue',fg='white',width=20,height=2,command=handle_sign_in_with_facebook)
login_btn.pack(pady=(3,20))
login_btn.config(font=('verdana',8))









 




root.mainloop()
