import pymysql

def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password='',
        port=3307,
        db='students',
    )
    return conn

def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    conn.close()
    return results

def add_student(studid, fname, lname, address, phone):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students VALUES (%s, %s, %s, %s, %s)", (studid, fname, lname, address, phone))
    conn.commit()
    conn.close()

def delete_student(studid):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE STUDID=%s", (studid,))
    conn.commit()
    conn.close()

def update_student(studid, fname, lname, address, phone, selectedStudid):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET STUDID=%s, FNAME=%s, LNAME=%s, ADDRESS=%s, PHONE=%s WHERE STUDID=%s", 
                   (studid, fname, lname, address, phone, selectedStudid))
    conn.commit()
    conn.close()

def reset_database():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students")
    conn.commit()
    conn.close()
