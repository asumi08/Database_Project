import customtkinter as ctk
from system import HealthRecordSystem
from patients import Patient

system = HealthRecordSystem(user='root', password='')

class PlaceholderEntry(ctk.CTkEntry):
    def __init__(self, *args, placeholder="", **kwargs):
        super().__init__(*args, **kwargs)
        self.placeholder = placeholder
        self.bind("<FocusIn>", self.clear_placeholder)
        self.bind("<FocusOut>", self.set_placeholder)
        self.set_placeholder()

    def clear_placeholder(self, event):
        if self.get() == self.placeholder:
            self.delete(0, ctk.END)
            self.configure(fg_color='white')  # Change text color to black

    def set_placeholder(self, event=None):
        if not self.get():
            self.insert(0, self.placeholder)
            self.configure(fg_color='lightgrey')  # Change text color to grey

class HealthRecordApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Health Record System")
        self.geometry("600x400")
        ctk.set_appearance_mode("dark")  # Set appearance mode to dark
        ctk.set_default_color_theme("blue")  # Set color theme

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.create_widgets()

    def create_widgets(self):
        self.name_entry = PlaceholderEntry(self.frame, placeholder="Patient Name")
        self.name_entry.pack(pady=5)

        self.age_entry = PlaceholderEntry(self.frame, placeholder="Patient Age")
        self.age_entry.pack(pady=5)

        self.gender_entry = PlaceholderEntry(self.frame, placeholder="Patient Gender")
        self.gender_entry.pack(pady=5)

        self.history_entry = PlaceholderEntry(self.frame, placeholder="Medical History")
        self.history_entry.pack(pady=5)

        self.blood_type_var = ctk.StringVar(value="A+") 

        self.blood_type_menu = ctk.CTkOptionMenu(
            self.frame,
            values=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
            command=self.set_blood_type
        )
        self.blood_type_menu.pack(pady=5)

        self.add_button = ctk.CTkButton(self.frame, text="Add Patient", command=self.add_patient)
        self.add_button.pack(pady=10)

        self.result_text = ctk.CTkTextbox(self.frame, width=50, height=10)
        self.result_text.pack(pady=10)

        self.blood_type = "A+"  # Initialize blood type

    def set_blood_type(self, value):
        self.blood_type = value

    def add_patient(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        medical_history = self.history_entry.get()

        if not age.isdigit():
            self.result_text.insert("1.0", "Please enter a valid age.\n")
            return

        patient = Patient(name, int(age), gender, medical_history)
        system.add_patient(patient, self.blood_type)
        self.result_text.insert("1.0", f"Patient {name} added successfully.\n")
        self.clear_entries()

    def clear_entries(self):
        self.name_entry.delete(0, "end")
        self.age_entry.delete(0, "end")
        self.gender_entry.delete(0, "end")
        self.history_entry.delete(0, "end")

