from tkinter import *
import sqlite3

root = Tk()
root.geometry('650x650')
root.title("Project Workshop")

ID=IntVar()
Fullname=StringVar()
Email=StringVar()
branch=StringVar()
var = IntVar()
var1= StringVar()
def show():
   connt = sqlite3.connect('conference.db')
   cursor = connt.cursor()
   cursor.execute('SELECT * FROM company')
   for row in cursor.fetchall():
      print(row)

def max_reg():
   con=sqlite3.connect('conference.db')
   cursor=con.cursor()
   cursor.execute('select conference,count(conference) from company group by conference order by count(conference) desc')
   count=0
   for row in cursor.fetchone():
      if count==0:
         print('The more people participated in conference is:')
         count=1
      if count==1:
         print(row)


def database():
   id1=ID.get()
   name1=Fullname.get()
   email=Email.get()
   Branch1=var.get()
   pho=var.get()
   prog=var1.get()
   conn = sqlite3.connect('conference.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS company (ID NUMBER(10) NOT NULL ,Fullname VARCHAR2(20),Email VARCHAR2(20),Branch VARCHAR2(20),Phone NUMBER(10) NOT NULL,conference varchar2(20),PRIMARY KEY(ID))')
   try :
      cursor.execute('INSERT  INTO company (ID,FullName,Email,Branch,Phone,conference)  VALUES(?,?,?,?,?,?)',(id1,name1,email,Branch1,pho,prog,))
   except :
      print('The user cannot enroll different course at same time.Sorry for inconivence caused !!! {} and your Id :- {}'.format(Branch1,prog))
   conn.commit()
   
             
label_0 = Label(root, text="COMPANY CONFERENCES",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="company NO",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=ID)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="company Name",width=20,font=("bold", 10))
label_2.place(x=100,y=180)

entry_2 = Entry(root,textvar=Fullname)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Email",width=20,font=("bold", 10))
label_3.place(x=90,y=230)

entry_3 = Entry(root,textvar=Email)
entry_3.place(x=240,y=230)

label_4 = Label(root, text="Phone",width=20,font=("bold", 10))
label_4.place(x=90,y=280)

entry_4 = Entry(root,textvar=var)
entry_4.place(x=240,y=280)

label_5= Label(root, text="Branch",width=20,font=("bold", 10))
label_5.place(x=385,y=330)

list1 = ['vizag','hyderbad','vijayawada'];
droplist=OptionMenu(root,branch, *list1)
droplist.config(width=15)
branch.set('select branch') 
droplist.place(x=500,y=330)

label_6= Label(root, text="conferences",width=20,font=("bold", 10))
label_6.place(x=100,y=330)

list1 = ['D.V.MANOR','MID CITY','GATE-WAY','NO-VOTEL'];

droplist=OptionMenu(root,var1, *list1)
droplist.config(width=15)
var1.set('select conference') 
droplist.place(x=240,y=330)

Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=380)

res=Button(root,padx=1,pady=1,text='click to show table',command=show,font=('none 10 bold'))
res.place(x=140,y=430)

res=Button(root,padx=1,pady=1,text='Max enroll workshop',command=max_reg,font=('none 10 bold'))
res.place(x=165,y=470)

root.mainloop()
