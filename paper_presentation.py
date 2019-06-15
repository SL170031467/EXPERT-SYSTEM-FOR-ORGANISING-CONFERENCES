from tkinter import *
import sqlite3
from sqlite3 import Error

root = Tk()
root.geometry('550x550')
root.title("PAPER PRESENTATIONS")
Author_name=StringVar()
presentation=StringVar()

def show():
   connt = sqlite3.connect('conference.db')
   cursor = connt.cursor()
   cursor.execute('SELECT * FROM presentation')
   for row in cursor.fetchall():
      print(row)
def database() :
    print("inside database")
    name=Author_name.get()
    print(name)
    presents=presentation.get()
    co = sqlite3.connect('conference.db')
    c=co.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS presentation(Author_name VARCHAR2(20),presentation VARCHAR2(20),PRIMARY KEY(Author_name))')
    try :
       c.execute('INSERT INTO presentation(Author_Name,presentation)  VALUES(?,?)',(name,presents))
    except :
       print('The user cannot enroll different presentations at same time.Sorry for inconivence caused !!! to your name {} for  :- {}'.format(name,presents),end=' ')
       print("And your presentation to do is ",end='')
       c.execute("select presentation from presentation where Author_name=?",(name,))
       result = c.fetchall()
       for row in result:
          print(row)
    co.commit()

label_0 = Label(root, text="paper presentations",width=40,font=("bold", 10))
label_0.place(x=90,y=53)
label_2 = Label(root, text="Author_Name",width=20,font=("bold", 10))
label_2.place(x=100,y=180)

entry_2 = Entry(root,textvar=Author_name)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="presentation",width=20,font=("bold", 10))
label_3.place(x=90,y=230)

entry_3 = Entry(root,textvar=presentation)
entry_3.place(x=240,y=230)
Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=230,y=350)
res=Button(root,padx=1,pady=1,text='click to show table',command=show,font=('none 10 bold'))
res.place(x=140,y=275)
root.mainloop()
