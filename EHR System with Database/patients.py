# patients.py
class Patient:
    def __init__(self, name, age, gender, medical_history):
        self.name = name
        self.age = age
        self.gender = gender
        self.medical_history = medical_history

    def to_string(self):
        return f"{self.name},{self.age},{self.gender},{self.medical_history}"
