from tkinter import *
import sqlite3

root = Tk()
root.geometry('900x600')
root.title("Registration Form")

Fullname = StringVar()
Email = StringVar()
var = StringVar()
c = StringVar()
var1 = StringVar()
Address = StringVar()
Phonenumber = StringVar()
months = StringVar()
days = StringVar()
year = StringVar()


def database():
    name1 = Fullname.get()
    email = Email.get()
    phone = Phonenumber.get()
    address = Address.get()
    DOBDay = days.get()
    DOBMonth = months.get()
    DOBYear = year.get()
    gender = var.get()
    country = c.get()
    prog = var1.get()
    conn = sqlite3.connect('Form.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT,'
        'Address TEXT,Phone TEXT,DOBDay TEXT,DOBMonth TEXT, DOBYear TEXT)')
    cursor.execute(
        'INSERT INTO Student (FullName,Email,Gender,country,Programming,Address,Phone, DOBDay, DOBMonth, '
        'DOBYear) VALUES(?,?,?,?,?,?,?,?,?,?)',
        (name1, email, gender, country, prog, address, phone, DOBDay, DOBMonth, DOBYear))
    conn.commit()


def dayss():
    dayss = list(range(1, 32))
    return dayss


def moonths():
    moonths = list(range(1, 13))
    return moonths


def yearr():
    yearr = list(range(1990, 2005))
    return yearr


label0 = Label(root, text="Registration Form", width=20, font=("bold", 20))
label0.place(x=290, y=53)

labela = Label(root, text="Address", width=20, font=("bold", 10))
labela.place(x=480, y=130)

entrya = Entry(root, textvar=Address, width=40)
entrya.place(x=640, y=130)

label1 = Label(root, text="Full Name", width=20, font=("bold", 10))
label1.place(x=80, y=130)

entry1 = Entry(root, textvar=Fullname, width=30)
entry1.place(x=240, y=130)

label2 = Label(root, text="Email", width=20, font=("bold", 10))
label2.place(x=68, y=180)

labelp = Label(root, text="Phone Number", width=20, font=("bold", 10))
labelp.place(x=480, y=180)

entryp = Entry(root, textvar=Phonenumber)
entryp.place(x=640, y=180)

entry2 = Entry(root, textvar=Email)
entry2.place(x=240, y=180)

label3 = Label(root, text="Gender", width=20, font=("bold", 10))
label3.place(x=70, y=230)

Radiobutton(root, text="Male", padx=5, variable=var, value="Male").place(x=235, y=230)
Radiobutton(root, text="Female", padx=20, variable=var, value="Female").place(x=290, y=230)

label4 = Label(root, text="country", width=20, font=("bold", 10))
label4.place(x=70, y=280)

list1 = ['Canada', 'India', 'UK', 'Nippal', 'Iceland', 'South Africa'];

droplist = OptionMenu(root, c, *list1)
droplist.config(width=25)
c.set('Select Your Country')
droplist.place(x=240, y=280)

label4 = Label(root, text="Language", width=20, font=("bold", 10))
label4.place(x=75, y=330)

list2 = ['C', 'C++', 'Java', 'Python']

droplist2 = OptionMenu(root, var1, *list2)
droplist2.config(width=25)
var1.set('Select Preffered Language')
droplist2.place(x=240, y=330)

labeldob = Label(root, text="Date Of Birth", width=20, font=("bold", 10))
labeldob.place(x=480, y=235)

days1 = dayss()
droplist3 = OptionMenu(root, days, *days1)
days.set("DD")
droplist3.place(x=640, y=230)

months1 = moonths()
droplist4 = OptionMenu(root, months, *months1)
months.set("MM")
droplist4.place(x=710, y=230)

year1 = yearr()
droplist5 = OptionMenu(root, year, *year1)
year.set("YYYY")
droplist5.place(x=790, y=230)

Button(root, text='Submit', width=20, bg='brown', fg='white', command=database).place(x=380, y=400)

root.mainloop()
