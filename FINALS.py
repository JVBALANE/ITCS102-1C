import time

print("HELLO!! I'M JV AND THIS IS MY CODE COMPILER PROGRAM\n=============================================")

while True:
    print("HERE ARE THE OPTIONS ON THE MENU:\n=============================================")
    print("A - PRINT STATEMENTS")
    print("B - VARIABLES")
    print("C - OPERATORS")
    print("D - CONDITIONAL STATEMENTS")
    print("E - LOOP")
    print("F - LIST")
    print("G - FUNCTIONS")
    print("X - EXIT")

    # Get input and convert it to uppercase to handle 'a' or 'A', 'x' or 'X'
    choice = input("Input your choice:  ").upper()

    if choice == "A":
        # Your code for Print Statements goes here
        print("Please Wait...")
        time.sleep(3)
        #upon learning sir, I found a timer that could make you wait to print on what you input, Just simply import time that you want 
        while True:
            print("\nOPTION 1 Submenu: ")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            sub_choice = input("Enter your choice:  ")
            if sub_choice == 'a':
                print("\nHere's the Definition of Print Statement:\nA Print Statement is a command in a programming language that displays output on a screen or other output device. It is a fundamental tool for debugging, displaying results, and interacting with users by showing them information during program execution.")

                continue
            elif sub_choice == 'b':
                print("\nHere's an example of Print Statement:\nprint:('HAPPY HOLIDAYS EVERYONE')\n#final output: HAPPY HOLIDAYS EVERYONE")

                continue
            elif sub_choice == 'c':
                print("\nPlease Wait...")
                time.sleep(3)

                break
            else:
                print("\nInvalid choice. Please enter a, b, or c.")

                continue

    elif choice == "B":
        print("\nPlease Wait...")
        time.sleep(3)
        while True:
            print("\nOPTION 2 Submenu: ")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            sub_choice = input("Enter your choice:  ")
            if sub_choice == 'a':
                print("\nHere's the Definition of Variables:\nIn Python, a variable is a named storage location in memory that holds a value. It acts as a label for data, allowing you to refer to and manipulate that data within your program. Variables are dynamically typed, meaning you don't need to explicitly declare their type; it's inferred from the value assigned to them. You can assign different types of data (like numbers, strings, lists, etc.) to a variable throughout the program.\n")

                continue
            elif sub_choice == 'b':
                print("\nHere's an example of Variables:\nExample Code for Variables: \nAge = 25\nprint(age)  # Output: 25

# Assigning a string to a variable
name = "John Doe"
print(name) # Output: John Doe

# Assigning a floating-point number to a variable
height = 5.9
print(height) # Output: 5.9

# Assigning a boolean value to a variable
is_student = True
print(is_student) # Output: True

               
                continue
            elif sub_choice == 'c':
                print("\nPlease Wait....")
                time.sleep(2)
                 
                break
            else:
                print("Invalid choice. Please enter a, b, or c.")

                continue
    elif choice == "C":
        print("\nPlease Wait....")
        time.sleep(2)
        while True:
             print("\nOption 3 Submenu: ")
             print("a - Definition")
             print("b - Example")
             print("c - Back to Main Menu")

             sub_choice = input("Enter your choice: ")
             if sub_choice == 'a':
                 print("\nOperators in Python are special symbols that perform specific operations \n on one or more operands (values or variables). Some common types of operators in \n Python include:Arithmetic operators:\n These operators perform mathematical operations such as \n addition (+), subtraction (-), multiplication (*), division (/), and modulus (%).\n")

                 continue
             elif sub_choice == 'b':
                 print("n1=eval(input(\"Enter the first number: \"))\nn2=eval(input(\"Enter the second number: \"))\ns=n1+n2\nd=n1-n2\np=n1*n2\nq=n1/n2\nprint(\"The sum of\",n1,\"and\",n2,\"is\",s)\nprint(\"The difference of\",n1,\"and\",n2,\"is\",d)\nprint(\"The product of\",n1,\"and\",n2,\"is\",p)\nprint(\"The quotient of\",n1,\"and\",n2,\"is\",q)\nprint(n1,\"exponent by\",n2,\"is\",n1**n2)\nprint(\"The remainder of\",n1,\"and\",n2,\"is\",n1%n2)\nprint(\"The floor division of\",n1,\"and\",n2,\"is\",n1 // n2)")

                 continue
             elif sub_choice == 'c':
                print("\nPlease Wait....")
                time.sleep(2)
                 
                break
             else:
                print("Invalid choice. Please enter a,b, or c.")
            

                continue

        
    elif choice == "D":
        # Your code for Conditional Statements goes here
        print("Please wait...")
        time.sleep(2)
        while True:
            print("Option 4 Submenu:")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            sub_choice=input("Input Your Choice")
            if sub_choice == 'a':
                print("\nIn Python, a conditional statement is a type of control flow statement that allows \n the program to make decisions based  on certain conditions. The basic syntax for a conditional \n statement is the 'if' statement. \n")

                continue

            elif sub_choice =='b':
                print("Conditionals in Python Examples:\n")
                print("x = 5 if x > 0:")
                print("x is positive.")

                continue
            
            elif sub_choice =='c':
                print("\nPlease Wait....")
                time.sleep(2)
                 
                break
            else:
                print("Invalid choice. Please enter a,b, or c.")
            
                continue

        continue
    elif choice == "E":
       print("\nPlease Wait....")
       time.sleep(2)
       while True:
            print("\nOption 5 Submenu: ")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            sub_choice = input("Enter your choice: ")
            if sub_choice == 'a':
                print("\nHere's the Definition of Loop:\nIn Python, a loop is a control flow statement that allows the program to \n execute a block of code multiple times. There are two types of loops in Python:\n the 'for' loop and the 'while' loop.\n")
                continue
            elif sub_choice == 'b':
                print("\nHere's an Example of Loop:\n]loop in Python Examples: \n")
                print("x = 5")
                print("while x > 0:")
                print("print(x)")
                print("x -= 1")
                continue
            elif sub_choice == 'c':
                print("\nPlease Wait....")
                time.sleep(2)
                 
                break
            else:
                print("\nInvalid choice. Please enter a, b, or c.")
                continue

    elif choice == "F":
        print("\nPlease Wait....")
        time.sleep(2)
        while True:
            print("\nOption 6 Submenu: ")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            sub_choice = input("Enter your choice: ")
            if sub_choice == 'a':
                print("Definition:\n")
                print("\nIn Python, a function is a block of reusable code that can be called by a program to \n perform a specific task. Functions are defined using the 'def' keyword, followed \n by the function name and a set of parentheses that  may include parameters.\n The code within the function is indented, \nand the function is typically defined before it is called.")

                continue

            elif sub_choice == 'b':
                print("Function in Python Examples: \n")
                print("def add(x, y):")
                print("result = x + y")
                print("return result")
                print("result = add(3, 4)")
                print("print(result)")

                continue

            elif sub_choice == 'c':
                print("\nPlease Wait....")
                time.sleep(2)
                 
                break

            else:
                print("\nInvalid choice. Please enter a, b, or c.")
                continue

    elif choice == "G":
        print("\nPlease Wait....")
        time.sleep(2)
        while True:
            print("\nOption 7 Submenu: ")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            sub_choice = input("Enter your choice: ")
            if sub_choice == 'a':
                print("Definition:\n")
                print("In Python, an array is a data structure that stores a collection of items of the same type.\n The items in an array are ordered and can be accessed by their index, which is an integer value that starts at 0.\n")
                
                continue
            
            elif sub_choice == 'b':
                print("Arrays in Python Examples: \n")
                print("from array import array")
                print("numbers = array('i', [1, 2, 3, 4, 5]")
                print("words = (['apple', 'banana', 'cherry']")
                print("words.append('orange')")
                print("words.insert(1, 'mango')")
                print("words.pop() ")
                print("words.remove('banana')")

                continue
 
            elif sub_choice == 'c':
                print("\nPlease Wait....")
                time.sleep(2)
                 
                break

            else:
                print("\nInvalid choice. Please enter a, b, or c.")
                continue


    elif choice == "X":
        print("\n====================================")
        print(" System Out. Thank you for using the compiler program!")
        print("====================================")
        break # This is the explicit stopping point
    else:
        print("Invalid choice. Please select from the menu options (A-G, X).")
        continue # Jumps back to the start of the loop and re-displays the menu
