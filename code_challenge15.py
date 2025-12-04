import os
import json
os.system('cls')
print("DLL STUDENT SYSTEM INFORMATION")
print("========================================")

stud_record = {}
while True:
    print("SELECT FROM FOLLOWING OPTIONS")
    print("A - Adding Student Record")
    print("B - Print All Record")
    print("C - Search Student Info")
    print("D - Delete Student Record")
    print("E - Print All Student Info")
    print("F - Export Data")
    print("G - Import Data")
    print("X - Exit System")

    choice = input("Input your choice: ").lower().strip()

    if choice == 'a':
        os.system('cls')
        print("ADD STUDENT RECORD")

        student_id = input("Input Student ID number: ").upper()
        first_name = input("Input Student first name: ").upper()
        last_name = input("Input Student last name: ").upper()
        course = input("Input Student course: ").upper()
        section = input("Input Student section: ").upper()
        email = input("Input Student email: ").upper()

        stud_record[student_id] = [first_name, last_name, course, section, email]
        print("DATA SAVED SUCCESFULLY\n")
        
        continue
    elif choice == 'b':
        os.system('cls')

        print("PRINTING STUDENT RECORD")
        print("========================================")

        for id, info in stud_record.items():
            print(f"STUDENT ID {id} - RECORD - {info}")

        continue
    elif choice == 'c':
        os.system('cls')
        print("SEARCH STUDENT RECORD")

        search_id = input("INPUT STUDENT ID:   ").lower()

        for each_student in stud_record.keys():
            if search_id in stud_record.keys():
                print("\n\nRECORD FOUND for {search_id}")
                print("======================================")
                for id in stud_record[search_id]:
                    print(f"-- {id}")
                print("======================================")
            else:
                print("NO RECORD FOUND")
            break
        continue
    elif choice == 'd':
        os.system('cls')
        print("DELETE STUDENT RECORD")

        search_id = input("INPUT STUDENT ID:   ").lower()

        for each_student in stud_record.keys():
            if search_id in stud_record.keys():
                print("\n\nRECORD FOUND for {search_id}")
                print("======================================")
                for id in stud_record[search_id]:
                    print(f"-- {id}")
                
                print("======================================")

                stud_record.pop(student_id)
                print("RECORD DELETED\n")
            else:
                print("NO RECORD FOUND\n")
            break
        continue
    elif choice == 'e':
        os.system('cls')
        print("EDIT / MODIFY STUDENT RECORD")

        search_id = input("INPUT STUDENT ID:   ").lower()

        for each_student in stud_record.keys():
            if search_id in stud_record.keys():
                print("\n\nRECORD FOUND for {search_id}")
                print("======================================")
                for id in stud_record[search_id]:
                    print(f"-- {id}")
                
                print("======================================")

                student_id = input("Input Student ID number: ").upper()
                first_name = input("Input student first name: ").upper()
                last_name = input("Input student last name: ").upper()
                course = input("Input student course: ").upper()
                section = input("Input student section: ").upper()
                email = input("Input student email: ").upper()

                stud_record[student_id] = [search_id][0] = first_name
                stud_record[student_id] = [search_id][1] = last_name
                stud_record[student_id] = [search_id][3] = course
                stud_record[student_id] = [search_id][4] = section 
                stud_record[student_id] = [search_id][5] = email
                print("DATA SAVED SUCCESFULLY\n")


            else:
                print("NO RECORD FOUND")
            break
        continue
    elif choice == 'f':
        print("EXPORT DATA")

        with open('student_record.json')as new_file:
            json.dump(stud_record, new_file, indent=4)
        print("DATA EXPORTED SUCCESFULLY\n")
        continue
    elif choice == 'g':
        print("IMPORT DATA")

        #json - javascript object notation (json) r - read
        with open ('student_record.json' , 'r') as new_file:
            imported_student = json.load(new_file)

        stud_record = imported_student
        print("DATA IMPORTED SUCCESSFULLY")
        continue
    elif choice == 'x':
        print("SYSTEM EXIT")
        break
    else:
        print("Invalid Choice, Re-enter code")
        continue
