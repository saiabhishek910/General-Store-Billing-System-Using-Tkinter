from tkinter import *
from tkinter import messagebox
import random
root=Tk()
root.title("Billing System")
root.geometry('1280x720')
bg_color='#4D0039'

#======================variable=================
c_name=StringVar()
c_phone=StringVar()
item=StringVar()
Rate=IntVar()
quantity=DoubleVar()
bill_no=StringVar()
x=random.randint(100,9999)
bill_no.set(str(x))

global l
l=[]

#=========================Functions================================

def additm():
    n=Rate.get()
    m=quantity.get()*n
    l.append(m)
    if item.get()!='' and Rate.get()>0 and quantity.get()>0:
        textarea.insert((10.0+float(len(l)-1)), f"{item.get()}\t\t{quantity.get()}\t\t{ m}\n")
    else:
        messagebox.showerror('Error','Please Enter Valid Product Details')


def gbill():
    if c_name.get() == "" or c_phone.get() == "":
        messagebox.showerror("Error", "Please Enter Customer Details")
    elif len(list(c_phone.get()))<=9:
        messagebox.showerror("Error", "Please Enter Valid Customer Phone Number")
    else:
        textAreaText = textarea.get(10.0,(10.0+float(len(l))))
        welcome()
        textarea.insert(END, textAreaText)
        textarea.insert(END, f"\n======================================")
        textarea.insert(END, f"\nTotal Payable Amount :\t\t      {sum(l)}")
        textarea.insert(END, f"\n\n======================================")
        save_bill()



def clear():
    c_name.set('')
    c_phone.set('')
    item.set('')
    Rate.set(0)
    quantity.set(0)
    welcome()
def exit():
    op = messagebox.askyesno("Exit", "Do You Really Want To Exit?")
    if op > 0:
        root.destroy()
def save_bill():
    op=messagebox.askyesno("Save bill","Do You To Save The Bill?")
    if op>0:
        bill_details=textarea.get('1.0',END)
        f1=open("bills/"+str(bill_no.get())+".txt","w")
        f1.write(bill_details)
        f1.close()
        messagebox.showinfo("Saved",f"Bill no, :{bill_no.get()} Saved Successfully")
    else:
        return
def welcome():
    textarea.delete(1.0,END)
    textarea.insert(END,"\t  Sri Sai Durga General Stores")
    textarea.insert(END,f"\n\nBill Number:\t\t{bill_no.get()}")
    textarea.insert(END,f"\nCustomer Name:\t\t{c_name.get()}")
    textarea.insert(END,f"\nPhone Number:\t\t{c_phone.get()}")
    textarea.insert(END,f"\n\n======================================")
    textarea.insert(END,"\nProduct\t\tQTY\t\tPrice")
    textarea.insert(END,f"\n======================================\n")
    textarea.configure(font='arial 15 bold')



title=Label(root,pady=2,text="Billing Software",bd=12,fg='White',bg='#2C3E50',font=('times new roman', 25 ,'bold'),relief=GROOVE,justify=CENTER)
title.pack(fill=X)

#=================Product Frames=================
F1=LabelFrame(root,bd=10,relief=GROOVE,text='Customer Details',font=('times new romon',15,'bold'),fg='White',bg='#2C3E50')
F1.place(x=0,y=80,relwidth=1)

cname_lbl=Label(F1,text='Customer Name',font=('times new romon',18,'bold'),fg='White',bg='#2C3E50').grid(row=0,column=0,padx=20,pady=5)
cname_txt=Entry(F1,width=15,textvariable=c_name,font='arial 15 bold',relief=SUNKEN,bd=7).grid(row=0,column=1,padx=10,pady=5)

cphone_lbl=Label(F1,text='Phone Number ',font=('times new romon',18,'bold'),fg='White',bg='#2C3E50').grid(row=0,column=2,padx=20,pady=5)
cphone_txt=Entry(F1,width=15,font='arial 15 bold',textvariable=c_phone,relief=SUNKEN,bd=7).grid(row=0,column=3,padx=10,pady=5)

F2 = LabelFrame(root, text='Product Details', font=('times new romon', 18, 'bold'),fg='White',bg='#2C3E50')
F2.place(x=20, y=180,width=630,height=500)

itm= Label(F2, text='Product Name', font=('times new romon',18, 'bold'),fg='White',bg='#2C3E50').grid(
row=0, column=0, padx=30, pady=20)
itm_txt = Entry(F2, width=20,textvariable=item, font='arial 15 bold', relief=SUNKEN, bd=7).grid(row=0, column=1, padx=10,pady=20)

rate= Label(F2, text='Product Price', font=('times new romon',18, 'bold'),fg='White',bg='#2C3E50').grid(
row=1, column=0, padx=30, pady=20)
rate_txt = Entry(F2, width=20,textvariable=Rate, font='arial 15 bold', relief=SUNKEN, bd=7).grid(row=1, column=1, padx=10,pady=20)

n= Label(F2, text='Product Quantity', font=('times new romon',18, 'bold'),fg='White',bg='#2C3E50').grid(
row=2, column=0, padx=30, pady=20)
n_txt = Entry(F2, width=20,textvariable=quantity, font='arial 15 bold', relief=SUNKEN, bd=7).grid(row=2, column=1, padx=10,pady=20)

#========================Bill area================
F3=Frame(root,relief=GROOVE,bd=10)
F3.place(x=700,y=180,width=500,height=500)

bill_title=Label(F3,text='Bill Area',font='arial 15 bold',bd=7,relief=GROOVE,fg='White',bg='#2C3E50').pack(fill=X)
scrol_y=Scrollbar(F3,orient=VERTICAL)
textarea=Text(F3,yscrollcommand=scrol_y,fg='White',bg='#2C3E50')
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=textarea.yview)
textarea.pack()
welcome()
#=========================Buttons======================
btn1=Button(F2,text='Add item',font='arial 15 bold',command=additm,padx=5,pady=10,bg='#F39C12', fg='#FFFFFF',width=15)
btn1.grid(row=3,column=0,padx=10,pady=30)
btn2=Button(F2,text='Generate Bill',font='arial 15 bold',command=gbill,padx=5,pady=10,bg='#F39C12', fg='#FFFFFF',width=15)
btn2.grid(row=3,column=1,padx=10,pady=30)
btn3=Button(F2,text='Clear',font='arial 15 bold',padx=5,pady=10,command=clear,bg='#F39C12', fg='#FFFFFF',width=15)
btn3.grid(row=4,column=0,padx=10,pady=30)
btn4=Button(F2,text='Exit',font='arial 15 bold',padx=5,pady=10,command=exit,bg='#F39C12', fg='#FFFFFF',width=15)
btn4.grid(row=4,column=1,padx=10,pady=30)

root.mainloop()
