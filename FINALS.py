import time

print("GREETINNGS FROM MY CODE COMPILER PROGRAM\n=============================================")

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
        print("Please Wait....")
        time.sleep(1)
        #upon learning sir, I found timer that make you wait to print what you input just import time above
        while True:
            print("\nOpton 1 Submenu: ")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            sub_choice = input("Enter your choice:  ")
            if sub_choice == 'a':
                print("\nHere's the Definition of Print Statement:\nThe print() function prints the specified message to the screen, or other standard output device. The message can be a string, or any other object, the object will be converted into a string before written to the screen.")

                continue
            elif sub_choice == 'b':
                print("\nHere's an example of Print Statement:\nHello World")

                continue
            elif sub_choice == 'c':
                print("\nPlease Wait....")
                time.sleep(2)

                break
            else:
                print("\nInvalid choice. Please enter a, b, or c.")

                continue

    elif choice == "B":
        print("\nPlease Wait....")
        time.sleep(2)
        while True:
            print("\nOption 2 Submenu: ")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            sub_choice = input("Enter your choice:  ")
            if sub_choice == 'a':
                print("\nHere's the Definition of Variables:\nIn Python, a variable is a name that refers to a value stored in memory. \nVariables are used to store and manipulate data in a program.\n")

                continue
            elif sub_choice == 'b':
                print("\nHere's an example of Variables:\nExample Code for Variables: \nName: ICAL\nAge: 18\nMarried: False\nTemperature: 38.1\n\nHi Ical\nYou're 18 years old\nFalse that you're married\nYour body temperature is 38.1 degrees celsius")

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
