from operator import index
import tkinter as tk
import time

window = tk.Tk()
window.title("My Profile")
window.configure(bg ="pink")
window.geometry("700x700")
window.resizable(False, True)

StudentTitle = tk.Label(text="Student Profile", font=("Myriad Pro", 30), padx=18, pady=18, bg="pink")
StudentName = tk.Label(text="Name: John Vincent P. Balane", font=("Myriad Pro", 20), pady=12, padx=8, bg="pink")
StudentAge = tk.Label(text="Age: 18", font=("Myriad Pro", 20), pady=12, padx=8, bg="pink")
StudentAddress = tk.Label(text="Address: Brgy. Ibabang Dupay, Lucena City", font=("Myriad Pro", 20), pady=12, padx=8, bg="pink")
StudentCourse = tk.Label(text="Course: BSIT", font=("Myriad Pro", 20), pady=12, padx=8, bg="pink")
StudentBirthdate = tk.Label(text="Birthdate: August 3, 2007", font=("Myriad Pro", 20), pady=12, padx=8, bg="pink")
StudentMottoLabel = tk.Label(text="Motto:", font=("Myriad Pro", 20), pady=12, padx=8, bg="pink")
StudentMotto= tk.Label(text="\tDream Big and Dare To Fail", font=("Myriad Pro", 20), pady=12, padx=8, bg="pink")

StudentTitle.pack(fill="both")
StudentName.pack(anchor='nw')
StudentAge.pack(anchor='nw')
StudentAddress.pack(anchor='nw')
StudentCourse.pack(anchor='nw')
StudentBirthdate.pack(anchor='nw')
StudentMottoLabel.pack(anchor='nw')
StudentMotto.pack(anchor='nw')

window. mainloop()
