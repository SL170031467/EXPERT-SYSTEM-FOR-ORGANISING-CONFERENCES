from tkinter import *
import sqlite3
root = Tk()
root.geometry('500x500')
root.title("My project")
def mod1():
        import part2
def mod2():
        import wor
def mod3():
    import sathish
print('----------------------------------choose any one of these-----------------------------------')
print('                                    1.registration                                          ')
print('                                    2.workshops                                             ')
print('                                    3.Presentations                                         ')
print('--------------------------------------------------------------------------------------------')
Button(root, text='Organisers registration form',width=20,bg='brown',fg='white',command=mod1).place(x=100,y=150)
Button(root, text='Workshops',width=20,bg='brown',fg='white',command=mod2).place(x=100,y=200)
Button(root, text='Presentations',width=20,bg='brown',fg='white',command=mod3).place(x=100,y=250)
