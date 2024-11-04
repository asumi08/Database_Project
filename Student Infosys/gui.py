from tkinter import *
from tkinter import ttk, messagebox
from student import add, delete, update, fetch_all, reset

class StudentRegistrationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Registration System")
        self.master.geometry("1080x720")
        self.master.configure(bg="#121212")

        self.ph1 = StringVar()
        self.ph2 = StringVar()
        self.ph3 = StringVar()
        self.ph4 = StringVar()
        self.ph5 = StringVar()
        self.search_var = StringVar()  

        self.create_widgets()
        self.refresh_table()

    def create_widgets(self):
        label = Label(self.master, text="Student Registration System", font=('Arial Bold', 30), fg="#0efefe", bg="#121212")
        label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

        label_params = {'font': ('Arial', 15), 'fg': '#0efefe', 'bg': '#121212'}
        studidLabel = Label(self.master, text="Student ID", **label_params)
        fnameLabel = Label(self.master, text="Firstname", **label_params)
        lnameLabel = Label(self.master, text="Lastname", **label_params)
        addressLabel = Label(self.master, text="Address", **label_params)
        phoneLabel = Label(self.master, text="Phone", **label_params)
        searchLabel = Label(self.master, text="Search", **label_params)  

        studidLabel.grid(row=3, column=0, padx=50, pady=5)
        fnameLabel.grid(row=4, column=0, padx=50, pady=5)
        lnameLabel.grid(row=5, column=0, padx=50, pady=5)
        addressLabel.grid(row=6, column=0, padx=50, pady=5)
        phoneLabel.grid(row=7, column=0, padx=50, pady=5)
        searchLabel.grid(row=9, column=0, padx=50, pady=5)  

        entry_params = {'width': 55, 'bd': 5, 'font': ('Arial', 15), 'bg': '#20232a', 'fg': '#0efefe'}
        self.studidEntry = Entry(self.master, textvariable=self.ph1, **entry_params)
        self.fnameEntry = Entry(self.master, textvariable=self.ph2, **entry_params)
        self.lnameEntry = Entry(self.master, textvariable=self.ph3, **entry_params)
        self.addressEntry = Entry(self.master, textvariable=self.ph4, **entry_params)
        self.phoneEntry = Entry(self.master, textvariable=self.ph5, **entry_params)
        self.searchEntry = Entry(self.master, textvariable=self.search_var, **entry_params)  

        self.studidEntry.grid(row=3, column=1, columnspan=4, padx=5)
        self.fnameEntry.grid(row=4, column=1, columnspan=4, padx=5)
        self.lnameEntry.grid(row=5, column=1, columnspan=4, padx=5)
        self.addressEntry.grid(row=6, column=1, columnspan=4, padx=5)
        self.phoneEntry.grid(row=7, column=1, columnspan=4, padx=5)
        self.searchEntry.grid(row=9, column=1, columnspan=4, padx=5)  

        button_params = {'padx': 65, 'pady': 25, 'width': 10, 'bd': 5, 'font': ('Arial', 15), 'fg': '#0efefe', 'bg': '#282c34', 'activebackground': '#00ffcc'}
        addBtn = Button(self.master, text="Add", command=self.add_student, **button_params)
        updateBtn = Button(self.master, text="Update", command=self.update_student, **button_params)
        deleteBtn = Button(self.master, text="Delete", command=self.delete_student, **button_params)
        resetBtn = Button(self.master, text="Reset", command=self.reset_data, **button_params)
        searchBtn = Button(self.master, text="Search", command=self.search_student, **button_params)
        selectBtn = Button(self.master, text="Select", command=self.select_student, **button_params)

        addBtn.grid(row=3, column=5, rowspan=2)
        updateBtn.grid(row=5, column=5, rowspan=2)
        deleteBtn.grid(row=7, column=5, rowspan=2)
        searchBtn.grid(row=9, column=5, rowspan=2)  
        resetBtn.grid(row=11, column=5, rowspan=2)
        selectBtn.grid(row=13, column=5, rowspan=2)

        self.my_tree = ttk.Treeview(self.master)
        self.my_tree['columns'] = ("Stud ID", "Firstname", "Lastname", "Address", "Phone")
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("Stud ID", anchor=W, width=170)
        self.my_tree.column("Firstname", anchor=W, width=150)
        self.my_tree.column("Lastname", anchor=W, width=150)
        self.my_tree.column("Address", anchor=W, width=165)
        self.my_tree.column("Phone", anchor=W, width=150)

        self.my_tree.heading("Stud ID", text="Student ID", anchor=W)
        self.my_tree.heading("Firstname", text="Firstname", anchor=W)
        self.my_tree.heading("Lastname", text="Lastname", anchor=W)
        self.my_tree.heading("Address", text="Address", anchor=W)
        self.my_tree.heading("Phone", text="Phone", anchor=W)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview.Heading", font=('Arial Bold', 15), foreground="#0efefe", background="#121212")
        style.configure("Treeview", background="#20232a", fieldbackground="#20232a", foreground="#0efefe")

        self.my_tree.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)

    def refresh_table(self):
        for data in self.my_tree.get_children():
            self.my_tree.delete(data)
        for array in fetch_all():
            self.my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    def add_student(self):
        studid = self.ph1.get()
        fname = self.ph2.get()
        lname = self.ph3.get()
        address = self.ph4.get()
        phone = self.ph5.get()
        message = add(studid, fname, lname, address, phone)
        messagebox.showinfo("Info", message)
        self.refresh_table()

    def update_student(self):
        selected_item = self.my_tree.selection()
        if not selected_item:
            messagebox.showinfo("Error", "Please select a data row")
            return
        selectedStudid = self.my_tree.item(selected_item[0])['values'][0]
        studid = self.ph1.get()
        fname = self.ph2.get()
        lname = self.ph3.get()
        address = self.ph4.get()
        phone = self.ph5.get()
        message = update(studid, fname, lname, address, phone, selectedStudid)
        messagebox.showinfo("Info", message)
        self.refresh_table()

    def delete_student(self):
        selected_item = self.my_tree.selection()
        if not selected_item:
            messagebox.showinfo("Error", "Please select a data row")
            return
        studid = self.my_tree.item(selected_item[0])['values'][0]
        message = delete(studid)
        messagebox.showinfo("Info", message)
        self.refresh_table()

    def reset_data(self):
        decision = messagebox.askquestion("Warning!!", "Delete all data?")
        if decision != "yes":
            return 
        message = reset()
        messagebox.showinfo("Info", message)
        self.refresh_table()

    def select_student(self):
        selected_item = self.my_tree.selection()
        if not selected_item:
            messagebox.showinfo("Error", "Please select a data row")
            return
        for index in range(5):
            self.ph1.set(self.my_tree.item(selected_item[0])['values'][index])

    def search_student(self):
        search_query = self.search_var.get().strip()
        for item in self.my_tree.get_children():
            self.my_tree.delete(item)

        for array in fetch_all():
            if search_query.lower() in array[0].lower() or search_query.lower() in array[1].lower():
                self.my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

def main():
    root = Tk()
    app = StudentRegistrationApp(root)
    root.mainloop()


