from database import add_student, delete_student, update_student, read, reset_database

def add(studid, fname, lname, address, phone):
    if any(field.strip() == "" for field in [studid, fname, lname, address, phone]):
        return "Error: Please fill up the blank entry"
    
    try:
        add_student(studid, fname, lname, address, phone)
        return "Student added successfully."
    except:
        return "Error: Stud ID already exists."

def delete(studid):
    delete_student(studid)
    return "Student deleted successfully."

def update(studid, fname, lname, address, phone, selectedStudid):
    return update_student(studid, fname, lname, address, phone, selectedStudid)

def fetch_all():
    return read()

def reset():
    reset_database()
    return "All data has been reset successfully."
