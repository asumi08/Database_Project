import mysql.connector

class HealthRecordSystem:
    def __init__(self, host='localhost', user='root', password='', database=''):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def add_patient(self, patient, blood_type):
        table_name = f"patients_{blood_type.lower()}"
        query = f"INSERT INTO {table_name} (name, age, gender, medical_history) VALUES (%s, %s, %s, %s)"
        values = (patient.name, patient.age, patient.gender, patient.medical_history)
        self.cursor.execute(query, values)
        self.connection.commit()
        print(f"Patient {patient.name} added successfully to {blood_type} table.")

    def search_patient_by_name(self, name):
        blood_types = ['a_pos', 'a_neg', 'b_pos', 'b_neg', 'ab_pos', 'ab_neg', 'o_pos', 'o_neg']
        found = False
        
        print(f"\nSearching for patient: {name}")
        for blood_type in blood_types:
            table_name = f"patients_{blood_type}"
            query = f"SELECT * FROM {table_name} WHERE name LIKE %s"
            self.cursor.execute(query, (name,))
            results = self.cursor.fetchall()

            if results:
                found = True
                print(f"\nBlood Type: {blood_type.upper()}")
                print("-" * 50)
                for row in results:
                    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Gender: {row[3]}, Medical History: {row[4]}")
        
        if not found:
            print(f"No records found for patient: {name}")

    def delete_patient(self, name, blood_type):
        table_name = f"patients_{blood_type.lower()}"
        query = f"DELETE FROM {table_name} WHERE name = %s"
        self.cursor.execute(query, (name,))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print(f"Patient {name} deleted successfully from {blood_type} table.")
        else:
            print(f"Patient {name} not found in {blood_type} table.")

    def print_all_patients(self):
        blood_types = ['a_pos', 'a_neg', 'b_pos', 'b_neg', 'ab_pos', 'ab_neg', 'o_pos', 'o_neg']
        
        print("\nAll Patient Records:")
        print("-" * 60)
        for blood_type in blood_types:
            table_name = f"patients_{blood_type}"
            query = f"SELECT * FROM {table_name}"
            self.cursor.execute(query)
            results = self.cursor.fetchall()

            if results:
                print(f"Blood Type: {blood_type.upper()}")
                print("-" * 50)
                for row in results:
                    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Gender: {row[3]}, Medical History: {row[4]}")
                print("\n")
            else:
                print(f"No records found in {blood_type.upper()} table.\n")

    def close(self):
        self.cursor.close()
        self.connection.close()
