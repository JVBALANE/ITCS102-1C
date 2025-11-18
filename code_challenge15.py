import os

print("DLL STUDENT INFORMATION SYSTEM")
print("---------------------------------------")
stud_info = {}

while True:
    print("SELECT THE FOLLOWING OPTIONS ")
    print("A - Add Student Record ")
    print("B - Search Student ")
    print("C - Edit Student Record ")
    print("D - Delete Student Record ")
    print("E - Print All Student Info ")
    print("F - Export Data ")
    print("G - Exit System ")
    
    choice = input("Select option from A - G --> ").lower().strip()

    if choice == 'a':
        print("ADD STUDENT RECORD")

        stud_id = input("Input Student ID: ")
        first_name = input("Type Your First Name: ").UPPER()
        mid_name = input("Type Your Middle Name: ").UPPER()
        last_name = input("Type Your Last Name: ").UPPER()
        section = ("Type Your Section: ").UPPER()
        email = ("Type Your Email: ")
        
        stud_info[stud_id] = [first_name, mid_name, last_name, section, email]
        print("DATA SAVE SUCCESSFULLY")
        os.system(cls)
        continue
    elif choice == 'b':
        pass
        continue
    elif choice == 'c':
        pass
        continue
    elif choice == 'd':
        pass
        continue
    elif choice == 'e':
        pass
        continue
    elif choice == 'f':
        pass
        continue
    elif choice == 'g':
        print("System Exit")
        break
    else:
        print("Invalid Choice")
        continue

        
        
