from tkinter import *
import mysql.connector as con
#import pandas as pd

style1 = ("myriad pro", 25, "bold", 'italic')
but_style=("myriad pro", 5, "bold")
label = ("myriad pro", 13, "bold")
entry=("myriad pro", 13)
style3 = ("calibre", 10, "bold")
win_size = '800x600'
title="cms"
heading="Customer Management System"
h,w=2,20
margin='black'
left_a='#dcdce0'
right_a='#ececf0'
tab_color='#f8f8f8'
tab_choosen='#ececf0'
but_color='cyan'

lite = con.connect(host="localhost", user="root", password="VASU__789", database="yogesh",auth_plugin='mysql_native_password')

if lite.is_connected():
    print(".............................. I am ON ..............................")
else:
    print(".............................. Database is offline ..............................")

mycon = lite.cursor()
customers=mycon.execute("SELECT Name from customers;")
customers_name=mycon.fetchall()
customers_names=tuple(customers_name)
print(customers_name)

customers=[]
name=None
address=None
date=None
phone=None
amount=None

# last date of customers
# Make sub divisions of employ management division

def Search_c2():
    sname=menu.get()
    try:
        if(sname=="Enter Name"):
            rid1.set("Nothing")
            print(f"{sname} \n {rid1}")
        else:
            pname=sname[1:-2]
            pulkit=mycon.execute("Select Name from customers where Name = %s;",(pname,))
            Puit=mycon.fetchall()
            rid1.set(Puit)
            print(Puit)
            print(pname)
            print(type(pname))
            lite.commit()

            pulkit1=mycon.execute(f"SELECT Address from customers where Name = %s;",(pname,))
            Puit1=mycon.fetchall()
            rname1.set(Puit1)
            
            pulkit2=mycon.execute("SELECT Address from customers where Name=%s;",(sname[1:-2],))
            Puit2=mycon.fetchall()
            rphone1.set(Puit2)

            # pulkit3=mycon.execute("SELECT Phone_number from customers where Name=%s;",(sname[1:-2],))
            # Puit3=mycon.fetchall()
            # radd1.set(Puit3)

            # pulkit4=mycon.execute("SELECT Amount from customers where Name=%s;",(sname[1:-2],))
            # Puit4=mycon.fetchall()
            # ramount1.set(Puit4)            

            # print(f"{Puit1},{sname[1:-2]},{Puit2},{sname[1:-2]},{Puit3},{sname},{Puit4}")
            # print("Sneha is bad")
    
    except Exception as e:
        print(e)
    
def S_no():
    query=mycon.execute("SELECT S_no FROM customers WHERE S_no=(SELECT max(S_no) FROM customers);")
    last_cus=mycon.fetchall()
    last=last_cus[0][0]
    return last

def rem_c2(Name):
    mycon.execute("DELETE FROM CUSTOMERS WHERE NAME='%s';",(Name,))
    lite.commit()

def add_c2(Entry1,Entry2,Entry3,Entry4,Entry5,Entry6):
    name=Entry1.get()
    address=Entry2.get()
    date=Entry3.get()
    amount=Entry4.get()
    phone=Entry5.get()
    attend=Entry6.get()
    print(name,address,date,amount,phone,attend)
    mycon.execute("INSERT INTO CUSTOMERS VALUES (%s,%s,%s,%s,%s,%s,%s)",(S_no()+1,name,address,date,amount,phone,attend))
    lite.commit()
    #mycon.close()
    Entry1.delete(0,END)
    Entry2.delete(0,END)
    Entry3.delete(0,END)
    Entry4.delete(0,END)
    Entry5.delete(0,END)
    S_no()

def notify():
    root =Tk()
    root.geometry(win_size)
    root.title("Customer Management System")
    root.resizable(height=False , width=False)
    root.config(background=margin)
    
    # Create Frame widget
    l_frame = Frame(root, width=200, height=400)
    l_frame.place(anchor=N,relx=0,x=95,y=0)
    l_frame.config(bg=right_a,height=600,width=190)
    
    r_frame = Frame(root, width=200, height=400)
    r_frame.place(anchor=N,relx=0,x=495,y=0)
    r_frame.config(bg=left_a,height=600,width=610)
        
    #search_b = Frame(root, highlightbackground = "black", highlightthickness =1)
    search=Button(root,text="Search Customer",command=lambda:[Search(),root.destroy],font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    search.place(anchor=N,relx=0,x=85,y=130)
    #search_b.place(anchor=N,relx=0,x=85,y=130)
    add_c=Button(root,text="Add Customer",font=label,height=h,width=w,background=tab_choosen,bd=1,default='active')
    add_c.place(anchor=N,relx=0,x=85,y=178)
    del_c=Button(root,text="Remove Customer",command=lambda:[rem_c1(),root.destroy],font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    del_c.place(anchor=N,relx=0,x=85,y=226)
    notify=Button(root,text="Notify Customer",font=label,height=h,width=w,background=tab_choosen,bd=1,default='disable')
    notify.place(anchor=N,relx=0,x=85,y=274)
    emp=Button(root,text="Employ Mangement",command=lambda:[emp_m_s(),root.destroy],font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    emp.place(anchor=N,relx=0,x=85,y=322)

def emp_m_s_m():
    root =Tk()
    root.geometry(win_size)
    root.title("Customer Management System")
    root.resizable(height=False , width=False)
    head=Label(root,text="Customer Enrollment",font=style1)
    head.place(anchor=N,relx=0.5,x=120,y=30)

    search=Button(root,text="Search Customer",command=lambda:[Search(),root.destroy],font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    search.place(anchor=N,relx=0,x=85,y=130)
    #search_b.place(anchor=N,relx=0,x=85,y=130)
    add_c=Button(root,text="Add Customer",command=lambda:[add_c1(),root.destroy],font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    add_c.place(anchor=N,relx=0,x=85,y=178)
    del_c=Button(root,text="Remove Customer",command=lambda:[rem_c1(),root.destroy],font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    del_c.place(anchor=N,relx=0,x=85,y=226)
    notify=Button(root,text="Notify Customer",font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    notify.place(anchor=N,relx=0,x=85,y=274)
    emp=Button(root,text="Employ Mangement +",command=lambda:[emp_m_s(),root.destroy],font=label,height=h,width=w,background=tab_choosen,bd=1,default='disable')
    emp.place(anchor=N,relx=0,x=85,y=324)
    manage_e=Button(root,text="Manage Employee",command=lambda:[emp_m_s_m(),root.destroy],font=label,height=h,width=w,background=tab_choosen,bd=1,default='disable')
    manage_e.place(anchor=N,relx=0,x=95,y=372)
    add_e=Button(root,text="Add employee",command=lambda:[emp_m_s_a(),root.destroy],font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    add_e.place(anchor=N,relx=0,x=95,y=420)

    mainloop()

def emp_m_s_a():
    root =Tk()
    root.geometry(win_size)
    root.title("Customer Management System")
    root.resizable(height=False , width=False)
    head=Label(root,text="Customer Enrollment",font=style1)
    head.place(anchor=N,relx=0.5,x=120,y=30)

    search=Button(root,text="Search Customer",command=lambda:[Search(),root.destroy],font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    search.place(anchor=N,relx=0,x=85,y=130)
    #search_b.place(anchor=N,relx=0,x=85,y=130)
    add_c=Button(root,text="Add Customer",command=lambda:[add_c1(),root.destroy],font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    add_c.place(anchor=N,relx=0,x=85,y=178)
    del_c=Button(root,text="Remove Customer",command=lambda:[rem_c1(),root.destroy],font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    del_c.place(anchor=N,relx=0,x=85,y=226)
    notify=Button(root,text="Notify Customer",font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    notify.place(anchor=N,relx=0,x=85,y=274)
    emp=Button(root,text="Employ Mangement +",command=lambda:[emp_m_s(),root.destroy],font=label,height=h,width=w,background=tab_choosen,bd=1,default='disable')
    emp.place(anchor=N,relx=0,x=85,y=324)
    manage_e=Button(root,text="Manage Employee",command=lambda:[emp_m_s_m(),root.destroy],font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    manage_e.place(anchor=N,relx=0,x=95,y=372)
    add_e=Button(root,text="Add employee",command=lambda:[emp_m_s_a(),root.destroy],font=label,height=h,width=w,background=tab_choosen,bd=1,default='disable')
    add_e.place(anchor=N,relx=0,x=95,y=420)

    mainloop()

def emp_m_s():
    root =Tk()
    root.geometry(win_size)
    root.title("Customer Management System")
    root.resizable(height=False , width=False)
    head=Label(root,text="Customer Enrollment",font=style1)
    head.place(anchor=N,relx=0.5,x=120,y=30)

    # Create Frame widget
    l_frame = Frame(root, width=200, height=400)
    l_frame.place(anchor=N,relx=0,x=95,y=0)
    l_frame.config(bg=right_a,height=600,width=190)
    
    r_frame = Frame(root, width=200, height=400)
    r_frame.place(anchor=N,relx=0,x=495,y=0)
    r_frame.config(bg=left_a,height=600,width=610)
        
    #search_b = Frame(root, highlightbackground = "black", highlightthickness =1)
    search=Button(root,text="Search Customer",command=lambda:[Search(),root.destroy],font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    search.place(anchor=N,relx=0,x=85,y=130)
    #search_b.place(anchor=N,relx=0,x=85,y=130)
    add_c=Button(root,text="Add Customer",command=lambda:[add_c1(),root.destroy],font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    add_c.place(anchor=N,relx=0,x=85,y=178)
    del_c=Button(root,text="Remove Customer",command=lambda:[rem_c1(),root.destroy],font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    del_c.place(anchor=N,relx=0,x=85,y=226)
    notify=Button(root,text="Notify Customer",font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    notify.place(anchor=N,relx=0,x=85,y=274)
    emp=Button(root,text="Employ Mangement +",command=lambda:[emp_m_s(),root.destroy],font=label,height=h,width=w,background=tab_choosen,bd=1,default='disable')
    emp.place(anchor=N,relx=0,x=85,y=324)
    manage_e=Button(root,text="Manage Employee",command=lambda:[emp_m_s_m(),root.destroy],font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    manage_e.place(anchor=N,relx=0,x=95,y=372)
    add_e=Button(root,text="Add employee",command=lambda:[emp_m_s_a(),root.destroy],font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    add_e.place(anchor=N,relx=0,x=95,y=420)

    mainloop()
    
def Search():
    root =Tk()
    root.geometry(win_size)
    root.title("Customer Management System")
    root.resizable(height=False , width=False)

    # Create Frame widget
    l_frame = Frame(root, width=200, height=400)
    l_frame.place(anchor=N,relx=0,x=95,y=0)
    l_frame.config(bg=right_a,height=600,width=190)
    
    r_frame = Frame(root, width=200, height=400)
    r_frame.place(anchor=N,relx=0,x=495,y=0)
    r_frame.config(bg=left_a,height=600,width=610)

    global rid1,radd1,rdate1,rphone1,ramount1,rname1
    rid1=StringVar()
    rname1=StringVar()
    radd1=StringVar()
    #rdate1=StringVar()  
    rphone1=StringVar()
    ramount1=StringVar()

    #search_b = Frame(root, highlightbackground = "black", highlightthickness =1)
    search=Button(root,text="Search Customer",font=label,height=h,width=w,background=tab_choosen,bd=1,default='disable')
    search.place(anchor=N,relx=0,x=85,y=130)
    #search_b.place(anchor=N,relx=0,x=85,y=130)
    add_c=Button(root,text="Add Customer",command=lambda:[add_c1(),root.destroy],font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    add_c.place(anchor=N,relx=0,x=85,y=178)
    del_c=Button(root,text="Remove Customer",command=lambda:[rem_c1(),root.destroy],font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    del_c.place(anchor=N,relx=0,x=85,y=226)
    notify=Button(root,text="Notify Customer",font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    notify.place(anchor=N,relx=0,x=85,y=274)
    emp=Button(root,text="Employ Mangement",command=lambda:[emp_m_s(),root.destroy],font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    emp.place(anchor=N,relx=0,x=85,y=322)

    head=Label(r_frame,text="Customer Enrollment",font=style1,bg=left_a)
    head.place(anchor=N,relx=0.5,y=30)
    Name=Label(r_frame,text="Name",font=label,background=left_a)
    Name.place(anchor=N,relx=0.5,x=-140,y=120)
    global menu
    
    menu=StringVar()
    menu.set("Enter Name")
    drop= OptionMenu(r_frame, menu,*customers_names)
    drop.place(anchor=N,relx=0.5,x=0,y=118)

    drop.config(width=30,bg='white',highlightbackground=left_a,fg='black')
    rid=Label(root,textvariable=rid1,font=style3)
    rid.place(anchor=N,relx=0.5,x=-180,y=238)
    rname=Label(root,textvariable=rname1,font=style3)
    rname.place(anchor=N,relx=0.5,x=-130,y=238)
    rnumber=Label(root,textvariable=rphone1,font=style3)
    rnumber.place(anchor=N,relx=0.5,x=-50,y=238)
    radd=Label(root,textvariable=radd1,font=style3)
    radd.place(anchor=N,relx=0.5,x=100,y=238)
    ramont=Label(root,textvariable=ramount1,font=style3)
    ramont.place(anchor=N,relx=0.5,x=200,y=238)

    rid1.set('None1')
    rname1.set('None2')
    rphone1.set('None3')
    radd1.set('None4')
    ramount1.set('None5')
    
    search=Button(r_frame,font=label,text="Search",command=lambda:[Search_c2()],background=left_a)
    search.place(anchor=N,relx=0.5,x=0,y=400)

    mainloop()

def rem_c1():
    root =Tk()
    root.geometry(win_size)
    root.title("Customer Management System")
    root.resizable(height=False , width=False)

    # Create Frame widget
    l_frame = Frame(root, width=200, height=400)
    l_frame.place(anchor=N,relx=0,x=95,y=0)
    l_frame.config(bg=right_a,height=600,width=190)
    
    r_frame = Frame(root, width=200, height=400)
    r_frame.place(anchor=N,relx=0,x=495,y=0)
    r_frame.config(bg=left_a,height=600,width=610)
        
    head=Label(r_frame,text="Customer Enrollment",font=style1,bg=left_a)
    head.place(anchor=N,relx=0.5,y=30)

    #search_b = Frame(root, highlightbackground = "black", highlightthickness =1)
    search=Button(root,text="Search Customer",command=lambda:[Search(),root.destroy],font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    search.place(anchor=N,relx=0,x=85,y=130)
    #search_b.place(anchor=N,relx=0,x=85,y=130)
    add_c=Button(root,text="Add Customer",command=lambda:[add_c1(),root.destroy],font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    add_c.place(anchor=N,relx=0,x=85,y=178)
    del_c=Button(root,text="Remove Customer",font=label,height=h,width=w,background=tab_choosen,bd=1,default='disable')
    del_c.place(anchor=N,relx=0,x=85,y=226)
    notify=Button(root,text="Notify Customer",font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    notify.place(anchor=N,relx=0,x=85,y=274)
    emp=Button(root,text="Employ Mangement",command=lambda:[emp_m_s(),root.destroy],font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    emp.place(anchor=N,relx=0,x=85,y=322)

    Name=Label(r_frame,text="Name",font=label,background=left_a)
    Name.place(anchor=N,relx=0.5,x=-90,y=120)
    menu= StringVar()
    menu.set("Enter Name")
    #Create a dropdown Menu
    drop= OptionMenu(r_frame, menu,*customers_names)
    drop.place(anchor=N,relx=0.5,x=50,y=118)
    drop.config(width=30,background='white',highlightbackground=left_a,fg='black')
    #menu.set(drop.active())

    search=Button(r_frame,font=label,text="Remove",background=but_color,command=lambda:[rem_c2(menu)])
    search.place(anchor=N,relx=0.5,x=0,y=400)

    mainloop()

def add_c1():
    root =Tk()
    root.geometry(win_size)
    root.title("Customer Management System")
    root.resizable(height=False , width=False)
    root.config(background=margin)
    
    # Create Frame widget
    l_frame = Frame(root, width=200, height=400)
    l_frame.place(anchor=N,relx=0,x=95,y=0)
    l_frame.config(bg=right_a,height=600,width=190)
    
    r_frame = Frame(root, width=200, height=400)
    r_frame.place(anchor=N,relx=0,x=495,y=0)
    r_frame.config(bg=left_a,height=600,width=610)
        
    #search_b = Frame(root, highlightbackground = "black", highlightthickness =1)
    search=Button(root,text="Search Customer",command=lambda:[Search(),root.quit()],font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    search.place(anchor=N,relx=0,x=85,y=130)
    #search_b.place(anchor=N,relx=0,x=85,y=130)
    add_c=Button(root,text="Add Customer",font=label,height=h,width=w,background=tab_choosen,bd=1,default='disable')
    add_c.place(anchor=N,relx=0,x=85,y=178)
    del_c=Button(root,text="Remove Customer",command=lambda:[root.quit(),rem_c1()],font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    del_c.place(anchor=N,relx=0,x=85,y=226)
    notify=Button(root,text="Notify Customer",font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    notify.place(anchor=N,relx=0,x=85,y=274)
    emp=Button(root,text="Employ Mangement",command=lambda:[root.quit(),emp_m_s()],font=label,height=h,width=w,background=tab_color,bd=1,default='active')
    emp.place(anchor=N,relx=0,x=85,y=322)

    head=Label(r_frame,text="Customer Enrollment",font=style1,background=left_a)
    head.place(anchor=N,relx=0.5,x=0,y=30)
    Name=Label(r_frame,text="Name",font=label,background=left_a)
    Name.place(anchor=N,relx=0.5,x=-120,y=120)
    Entry1=Entry(r_frame,font=entry,textvariable=name)                       #,textvariable=name
    Entry1.place(anchor=N,relx=0.5,x=0,y=120)
    
    Address=Label(r_frame,text="Address",font=label,background=left_a)
    Address.place(anchor=N,relx=0.5,x=-130,y=170)
    Entry2=Entry(r_frame,font=entry)                       #,textvariable=name
    Entry2.place(anchor=N,relx=0.5,x=0,y=170)
    
    idate=Label(r_frame,text="Date Of Joining",font=label,background=left_a)
    idate.place(anchor=N,relx=0.5,x=-160,y=220)
    #idate_f=Label(r_frame,text="YYYY/MM/DD",font=label,background=left_a)
    #idate_f(anchor=N,relx=0.5,x=100,y=220)
    Entry3=Entry(r_frame,font=entry)                       #,textvariable=name
    Entry3.place(anchor=N,relx=0.5,x=0,y=220)

    amount=Label(r_frame,text="Amount Paid",font=label,background=left_a)
    amount.place(anchor=N,relx=0.5,x=-150,y=270)
    Entry4=Entry(r_frame,font=entry)                       #,textvariable=name
    Entry4.place(anchor=N,relx=0.5,x=0,y=270)
    
    Phone_no=Label(r_frame,text="Phone Number",font=label,background=left_a)
    Phone_no.place(anchor=N,relx=0.5,x=-160,y=320)
    Entry5=Entry(r_frame,font=entry)                       #,textvariable=name
    Entry5.place(anchor=N,relx=0.5,x=0,y=320)
    
    attendend=Label(r_frame,text="Attended By",font=label,background=left_a)
    attendend.place(anchor=N,relx=0.5,x=-150,y=370)
    employee=StringVar()
    employee.set("Choose employee")
    print(employee)
    emp=[('Ashish'),('Adil')]
    Entry6=OptionMenu(r_frame,employee,*emp)                       #,textvariable=name
    Entry6.place(anchor=N,relx=0.5,x=0,y=370)                      # Python, the * operator is used to unpack elements from an iterable (like a list or tuple) into function arguments
    Entry6.config(width=24,bg='white',highlightbackground=left_a,fg='black')
    #employee.set(Entry6)

    submit=Button(r_frame,text="Submit",command=lambda:[add_c2(Entry1,Entry2,Entry3,Entry4,Entry5,employee)],font=label,height=2,width=10,bg=but_color)
    submit.place(anchor=N,relx=0.5,x=0,y=500)

    mainloop()

Search()
#rem_c1()