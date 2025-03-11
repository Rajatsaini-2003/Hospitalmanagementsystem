import tkinter as tk
from tkinter import messagebox
import sqlite3

def setup_database():
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS patients (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER,
                    gender TEXT,
                    diagnosis TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS doctors (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    specialty TEXT,
                    phone TEXT)''')
    conn.commit()
    conn.close()

def add_patient():
    name = entry_name.get()
    age = entry_age.get()
    gender = entry_gender.get()
    diagnosis = entry_diagnosis.get()

    if name and age and gender and diagnosis:
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()
        c.execute("INSERT INTO patients (name, age, gender, diagnosis) VALUES (?, ?, ?, ?)",
                  (name, age, gender, diagnosis))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Patient Added Successfully")
        clear_patient_fields()
    else:
        messagebox.showwarning("Input Error", "Please fill in all the fields")

def add_doctor():
    name = entry_doc_name.get()
    specialty = entry_specialty.get()
    phone = entry_phone.get()

    if name and specialty and phone:
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()
        c.execute("INSERT INTO doctors (name, specialty, phone) VALUES (?, ?, ?)",
                  (name, specialty, phone))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Doctor Added Successfully")
        clear_doctor_fields()
    else:
        messagebox.showwarning("Input Error", "Please fill in all the fields")

def view_patients():
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    c.execute("SELECT * FROM patients")
    patients = c.fetchall()
    conn.close()

    patients_list.delete(1.0, tk.END)  
    for patient in patients:
        patients_list.insert(tk.END, f"ID: {patient[0]}, Name: {patient[1]}, Age: {patient[2]}, Gender: {patient[3]}, Diagnosis: {patient[4]}\n")

def view_doctors():
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    c.execute("SELECT * FROM doctors")
    doctors = c.fetchall()
    conn.close()

    doctors_list.delete(1.0, tk.END)  
    for doctor in doctors:
        doctors_list.insert(tk.END, f"ID: {doctor[0]}, Name: {doctor[1]}, Specialty: {doctor[2]}, Phone: {doctor[3]}\n")

def clear_patient_fields():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_gender.delete(0, tk.END)
    entry_diagnosis.delete(0, tk.END)

def clear_doctor_fields():
    entry_doc_name.delete(0, tk.END)
    entry_specialty.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

window = tk.Tk()
window.title("Hospital Management System")

setup_database()

patient_frame = tk.LabelFrame(window, text="Patient Information", padx=10, pady=10)
patient_frame.grid(row=0, column=0, padx=20, pady=20)

tk.Label(patient_frame, text="Name").grid(row=0, column=0)
entry_name = tk.Entry(patient_frame)
entry_name.grid(row=0, column=1)

tk.Label(patient_frame, text="Age").grid(row=1, column=0)
entry_age = tk.Entry(patient_frame)
entry_age.grid(row=1, column=1)

tk.Label(patient_frame, text="Gender").grid(row=2, column=0)
entry_gender = tk.Entry(patient_frame)
entry_gender.grid(row=2, column=1)

tk.Label(patient_frame, text="Diagnosis").grid(row=3, column=0)
entry_diagnosis = tk.Entry(patient_frame)
entry_diagnosis.grid(row=3, column=1)

add_patient_button = tk.Button(patient_frame, text="Add Patient", command=add_patient)
add_patient_button.grid(row=4, column=0, columnspan=2)

doctor_frame = tk.LabelFrame(window, text="Doctor Information", padx=10, pady=10)
doctor_frame.grid(row=1, column=0, padx=20, pady=20)

tk.Label(doctor_frame, text="Name").grid(row=0, column=0)
entry_doc_name = tk.Entry(doctor_frame)
entry_doc_name.grid(row=0, column=1)

tk.Label(doctor_frame, text="Specialty").grid(row=1, column=0)
entry_specialty = tk.Entry(doctor_frame)
entry_specialty.grid(row=1, column=1)

tk.Label(doctor_frame, text="Phone").grid(row=2, column=0)
entry_phone = tk.Entry(doctor_frame)
entry_phone.grid(row=2, column=1)

add_doctor_button = tk.Button(doctor_frame, text="Add Doctor", command=add_doctor)
add_doctor_button.grid(row=3, column=0, columnspan=2)

view_patients_button = tk.Button(window, text="View Patients", command=view_patients)
view_patients_button.grid(row=2, column=0, padx=20, pady=20)

view_doctors_button = tk.Button(window, text="View Doctors", command=view_doctors)
view_doctors_button.grid(row=3, column=0, padx=20, pady=20)

patients_list = tk.Text(window, height=10, width=50)
patients_list.grid(row=4, column=0, padx=20, pady=20)

doctors_list = tk.Text(window, height=10, width=50)
doctors_list.grid(row=5, column=0, padx=20, pady=20)

window.mainloop()