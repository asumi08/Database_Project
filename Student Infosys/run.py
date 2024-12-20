import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password='',
        port=3307,
        db='students',
    )
    return conn

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)
    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")
    my_tree.tag_configure('orow', background='#f9f9f9', font=('Arial', 12), foreground="#000000")
    my_tree.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)

root = Tk()
root.title("Student Registration System")
root.geometry("1080x720+1200+300")
root.configure(bg="#ffffff")
root.resizable(False,False)
my_tree = ttk.Treeview(root)

ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()

def setph(word, num):
    if num == 1:
        ph1.set(word)
    elif num == 2:
        ph2.set(word)
    elif num == 3:
        ph3.set(word)
    elif num == 4:
        ph4.set(word)
    elif num == 5:
        ph5.set(word)

def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def add():
    studid = str(studidEntry.get())
    fname = str(fnameEntry.get())
    lname = str(lnameEntry.get())
    address = str(addressEntry.get())
    phone = str(phoneEntry.get())
    if (studid == "" or studid == " ") or (fname == "" or fname == " ") or (lname == "" or lname == " ") or (address == "" or address == " ") or (phone == "" or phone == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO students VALUES ('"+studid+"','"+fname+"','"+lname+"','"+address+"','"+phone+"') ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Student ID already exist")
            return
    refreshTable()

def reset():
    decision = messagebox.askquestion("Warning!!", "Delete all data?")
    if decision != "yes":
        return 
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occurred")
            return
        refreshTable()

def delete():
    decision = messagebox.askquestion("Warning!!", "Delete the selected data?")
    if decision != "yes":
        return 
    else:
        selected_item = my_tree.selection()[0]
        deleteData = str(my_tree.item(selected_item)['values'][0])
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students WHERE STUDID='"+str(deleteData)+"'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occurred")
            return
        refreshTable()

def select():
    try:
        selected_item = my_tree.selection()[0]
        studid = str(my_tree.item(selected_item)['values'][0])
        fname = str(my_tree.item(selected_item)['values'][1])
        lname = str(my_tree.item(selected_item)['values'][2])
        address = str(my_tree.item(selected_item)['values'][3])
        phone = str(my_tree.item(selected_item)['values'][4])
        setph(studid,1)
        setph(fname,2)
        setph(lname,3)
        setph(address,4)
        setph(phone,5)
    except:
        messagebox.showinfo(" Error", "Please select a data row")

def search():
    studid = str(studidEntry.get())
    fname = str(fnameEntry.get())
    lname = str(lnameEntry.get())
    address = str(addressEntry.get())
    phone = str (phoneEntry.get())
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE STUDID='"+studid+"' or FNAME='"+fname+"' or LNAME='"+lname+"' or ADDRESS='"+address+"' or PHONE='"+phone+"' ")
    try:
        result = cursor.fetchall()
        for num in range(0,5):
            setph(result[0][num],(num+1))
        conn.commit()
        conn.close()
    except:
        messagebox.showinfo("Error", "No data found")

def update():
    selectedStudid = ""
    try:
        selected_item = my_tree.selection()[0]
        selectedStudid = str(my_tree.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Error", "Please select a data row")
    studid = str(studidEntry.get())
    fname = str(fnameEntry.get())
    lname = str(lnameEntry.get())
    address = str(addressEntry.get())
    phone = str(phoneEntry.get())
    if (studid == "" or studid == " ") or (fname == "" or fname == " ") or (lname == "" or lname == " ") or (address == "" or address == " ") or (phone == "" or phone == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE students SET STUDID='"+studid+"', FNAME='"+fname+"', LNAME='"+lname+"', ADDRESS='"+address+"', PHONE='"+phone+"' WHERE STUDID='"+selectedStudid+"' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Student ID already exist")
            return
    refreshTable()


label = Label(root, text="Student Registration System", font=('Arial Bold', 30), fg="#000000", bg="#ffffff")
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

label_params = {'font': ('Arial', 15), 'fg': '#000000', 'bg': '#ffffff'}
studidLabel = Label(root, text="Student ID", **label_params)
fnameLabel = Label(root, text="First Name", **label_params)
lnameLabel = Label(root, text="Last Name", **label_params)
addressLabel = Label(root, text="Address", **label_params)
phoneLabel = Label(root, text="Phone", **label_params)

studidLabel.grid(row=3, column=0, padx=50, pady=5)
fnameLabel.grid(row=4, column=0, padx=50, pady=5)
lnameLabel.grid(row=5, column=0, padx=50, pady=5)
addressLabel.grid(row=6, column=0, padx=50, pady=5)
phoneLabel.grid(row=7, column=0, padx=50, pady=5)

entry_params = {'width': 55, 'bd': 5, 'font': ('Arial', 15), 'bg': '#f9f9f9', 'fg': '#000000'}
studidEntry = Entry(root, textvariable=ph1, **entry_params)
fnameEntry = Entry(root, textvariable=ph2, **entry_params)
lnameEntry = Entry(root, textvariable=ph3, **entry_params)
addressEntry = Entry(root, textvariable=ph4, **entry_params)
phoneEntry = Entry(root, textvariable=ph5, **entry_params)

studidEntry.grid(row=3, column=1, columnspan=4, padx=5)
fnameEntry.grid(row=4, column=1, columnspan=4, padx=5)
lnameEntry.grid(row=5, column=1, columnspan=4, padx=5)
addressEntry.grid(row=6, column=1, columnspan=4, padx=5)
phoneEntry.grid(row=7, column=1, columnspan=4, padx=5)

button_params = {'padx': 65, 'pady': 25, 'width': 10, 'bd': 5, 'font': ('Arial', 15), 'fg': '#000000', 'bg': '#4CAF50', 'activebackground': '#00ffcc'}
addBtn = Button(root, text="Add", command=add, **button_params)
updateBtn = Button(root, text="Update", command=update, **button_params)
deleteBtn = Button(root, text="Delete", command=delete, **button_params)
searchBtn = Button(root, text="Search", command=search, **button_params)
resetBtn = Button(root, text="Reset", command=reset, **button_params)
selectBtn = Button(root, text="Select", command=select, **button_params)

addBtn.grid(row=3, column=5, rowspan=2)
updateBtn.grid(row=5, column=5, rowspan=2)
deleteBtn.grid(row=7, column=5, rowspan=2)
searchBtn.grid(row=9, column=5, rowspan=2)
resetBtn.grid(row=11, column=5, rowspan=2)
selectBtn.grid(row=13, column=5, rowspan=2)

style = ttk.Style()
style.theme_use("default")
style.configure("Treeview.Heading", font=('Arial Bold', 15), fg="#000000", bg="#ffffff")
style.configure("Treeview", bg="#f9f9f9", fieldbackground="#f9f9f9", fg="#000000")

tree_frame = Frame(root, borderwidth=2, relief='solid', bg="#ffffff")
tree_frame.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)


my_tree = ttk.Treeview(tree_frame)

my_tree['columns'] = ("Student ID", "First Name", "Last Name", "Address", "Phone")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Student ID", anchor=W, width=170)
my_tree.column("First Name", anchor=W, width=150)
my_tree.column("Last Name", anchor=W, width=150)
my_tree.column("Address", anchor=W, width=165)
my_tree.column("Phone", anchor=W, width=150)

my_tree.heading("Student ID", text="Student ID", anchor=W)
my_tree.heading("First Name", text="First Name", anchor=W)
my_tree.heading("Last Name", text="Last Name", anchor=W)
my_tree.heading("Address", text="Address", anchor=W)
my_tree.heading("Phone", text="Phone", anchor=W)

refreshTable()
root.mainloop()