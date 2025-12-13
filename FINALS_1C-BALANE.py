import os
import time

def clear():
    # Clears the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

time.sleep(2)
clear()
print("HELLO, I'M JOHN VINCENT. THIS IS MY PYTHON CODE COMPILER SYSTEM")
time.sleep(2)
username = input("Enter your name: ")
# Standardizing the input prompt
use = input(f"Hi {username}, do you want to use the system? (yes/no): ").lower()

if use != 'yes':
    print("System exited.")
    time.sleep(2)
    # Use quit() or sys.exit() for a clean exit, but exit() is acceptable here.
    exit()

while True:
    clear()
    print("\n================== PYTHON LEARNING SYSTEM ===============")
    print("\tA - PRINT FUNCTION")
    print("\tB - DICTIONARY")
    print("\tC - FOR LOOP")
    print("\tD - EVAL FUNCTION")
    print("\tE - LOOP")
    print("\tF - LIST")
    print("\tG - INT FUNCTION")
    print("\tH - STRING CONCATENATION")
    print("\tI - EQUATIONS")
    print("\tJ - WHILE LOOP")
    print("\tK - IF STATEMENT")
    print("\tL - NESTED FOR LOOP")
    print("=========================================================")
    print("\tX - Exit")

    time.sleep(2)
    choice = input("Input your choice: ").upper()

    if choice == "A":
        while True:
            clear()
            print("\nOPTION 1 Submenu: PRINT FUNCTION")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            time.sleep(2)
            sub_choice = input("Enter your choice: ").lower()

            if sub_choice == 'a':
                # Definition
                print("\nPRINT: As described previously, the print() function is a built-in tool used to output data or text to a standard output location, typically the user's console.")
                print("It converts data to a string representation for display and, by default, adds a newline character at the end of the output.")
                time.sleep(2)
                input("\nPress Enter to continue...")

            elif sub_choice == 'b':
                # Example - Fixed syntax issues like { to " and added missing quotes/commas for execution context.
                
                print("Input:")
                
                
                print('name = "Vincent"')
                print("age = 18")
                # Corrected print statements to use proper function syntax and separators
                print('print("Name:", name, "Age:", age)')
                print('print("Hobbies:")')
                print('print("Cycling", "Basketball", "Badminton")')
                print('print("Favorite Fruits:")')
                print('print("Apple", "Banana", "Grapes", "Jackfruit", sep=" | ")')


                print("\nOutput:")
                
                
                print("Name: Vincent Age: 18")
                print("Hobbies:")
                print("Cycling Basketball Badminton")
                print("Favorite Fruits:")
                print("Apple | Banana | Grapes | Jackfruit")

                time.sleep(2)
                input("\nPress Enter to continue...")

            elif sub_choice == 'c':
                break
            else:
                print("Invalid choice.")
                time.sleep(2)

    elif choice == "B":
        while True:
            clear()
            print("\nOPTION 2 Submenu: DICTIONARY")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            time.sleep(2)
            sub_choice = input("Enter your choice: ").lower()

            if sub_choice == 'a':
                # Definition
                print("\nDICTIONARY: In Python, a dictionary is a built-in data structure that stores collections of key-value pairs. Each key within a dictionary must be unique and immutable (like a string or number), while the corresponding values can be any Python object. Dictionaries are defined using curly braces {} and provide efficient ways to look up, insert, or delete values based on their associated keys.")
                time.sleep(2)
                input("\nPress Enter...")

            elif sub_choice == 'b':
                # Example (The example code block itself was not indented, so I've formatted it as a clear simulated input/output)
                
                
                print("Input:")
                
                
                print('student = {')
                print('    "name": "Alice",')
                print('    "age": 20,')
                print('    "major": "Computer Science"')
                print('}')
                print('print(f"Name: {student[\'name\']}")')
                print('print(f"Age: {student[\'age\']}")')
                print('print(f"Major: {student[\'major\']}")')
                print('student["age"] = 21')
                print('student["gpa"] = 3.8')
                print('print("\\nUpdated student information:")')
                print('print(student)')
                print('del student["major"]')
                print('print("\\nStudent information after removing major:")')
                print('print(student)')
                print('print("\\nDictionary length:", len(student))')
                print('print("Keys:", student.keys())')
                print('print("Values:", student.values())')
                print('print("Items:", student.items())')
                print('if "name" in student:')
                print('    print("\\nStudent name exists in the dictionary.")')

                
                
                print("\nOutput:")
                
                
                print("Name: Alice")
                print("Age: 20")
                print("Major: Computer Science")
                print("\nUpdated student information:")
                print("{'name': 'Alice', 'age': 21, 'major': 'Computer Science', 'gpa': 3.8}")
                print("\nStudent information after removing major:")
                print("{'name': 'Alice', 'age': 21, 'gpa': 3.8}")
                print("\nDictionary length: 3")
                print("Keys: dict_keys(['name', 'age', 'gpa'])")
                print("Values: dict_values(['Alice', 21, 3.8])")
                print("Items: dict_items([('name', 'Alice'), ('age', 21), ('gpa', 3.8)])")
                print("\nStudent name exists in the dictionary.")

                time.sleep(2)
                input("\nPress Enter to continue...")


            elif sub_choice == 'c':
                break
            else:
                print("Invalid choice.")
                time.sleep(2)

    elif choice == "C":
        while True:
            clear()
            print("\nOPTION 3 Submenu: FOR LOOP")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            time.sleep(2)
            sub_choice = input("Enter your choice: ").lower()

            if sub_choice == 'a':
                # Definition
                print("\nFOR LOOP: A for loop in Python is a control flow statement used to iterate over a sequence (like a list, tuple, or string) or other iterable objects. It allows you to execute a block of code repeatedly, once for each item in the sequence. The loop continues until all items in the sequence have been processed.")
                time.sleep(2)
                input("\nPress Enter...")

            elif sub_choice == 'b':
                # Example (Fixed formatting and escaping)
               
                
                print("Input:")
              
                
                print("test_scores = [82, 94, 77, 89, 91, 73]")
                print("total_score = 0")
                print("score_count = len(test_scores)")
                print("for score in test_scores:")
                print("    total_score += score")
                print('    print(f"Added score {score} | Current total: {total_score}")')
                print("average_score = total_score / score_count")
                print('print("\\n--- Final Results ---")')
                print('print(f"Total of all test scores: {total_score}")')
                print('print(f"Number of test scores: {score_count}")')
                print('print(f"Average test score: {round(average_score, 2)}")')

                
                
                print("\nOutput:")
                
                
                print("Added score 82 | Current total: 82")
                print("Added score 94 | Current total: 176")
                print("Added score 77 | Current total: 253")
                print("Added score 89 | Current total: 342")
                print("Added score 91 | Current total: 433")
                print("Added score 73 | Current total: 506")
                print("\n--- Final Results ---")
                print("Total of all test scores: 506")
                print("Number of test scores: 6")
                print("Average test score: 84.33")

                time.sleep(2)
                input("\nPress Enter to continue...")

            elif sub_choice == 'c':
                break
            else:
                print("Invalid choice.")
                time.sleep(2)

    elif choice == "D":
        while True:
            clear()
            print("\nOPTION 4 Submenu: EVAL FUNCTION")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            time.sleep(2)
            sub_choice = input("Enter your choice: ").lower()

            if sub_choice == 'a':
                # Definition
                print("\nEVAL FUNCTION: The eval() function in Python is a built-in function that evaluates a string as a Python expression. It parses the string and executes it as if it were Python code, returning the result of the expression. Because of the possibility of executing arbitrary code, using eval() with untrusted input can pose significant security risks.")
                time.sleep(2)
                input("\nPress Enter...")

            elif sub_choice == 'b':
                # Example (Fixed print statements and variable usage)
                
                print("Input:")
                
                
                print("x = 12")
                print("y = 4")
                print('expr1 = "x + y"')
                print('expr2 = "x * y - 8"')
                print('expr3 = "(x // y) + (x % y)"')
                print('expr4 = "x > y"')
                # To simulate the actual execution and print the results correctly, I had to slightly adjust the variable names in the print statement to avoid errors during simulation printing.
                print('result1 = eval(expr1)')
                print('result2 = eval(expr2)')
                print('result3 = eval(expr3)')
                print('result4 = eval(expr4)')
                print('print(f"Using variables: x = 12, y = 4\\n")') # Simulating f-string
                print('print(f"Result of {expr1}: {result1}")')
                print('print(f"Result of {expr2}: {result2}")')
                print('print(f"Result of {expr3}: {result3}")')
                print('print(f"Result of {expr4}: {result4}")')

                
                print("\nOutput:")
                
                
                print("Using variables: x = 12, y = 4")
                print("\nResult of x + y: 16")
                print("Result of x * y - 8: 40")
                print("Result of (x // y) + (x % y): 3") # (12 // 4) is 3, (12 % 4) is 0, so result is 3. Note: The user's output of 12 for expr3 was incorrect. I kept the user's expression but simulated the correct output.
                print("Result of x > y: True")

                time.sleep(2)
                input("\nPress Enter to continue...")

            elif sub_choice == 'c':
                break
            else:
                print("Invalid choice.")
                time.sleep(2)

    elif choice == "E":
        while True:
            clear()
            print("\nOPTION 5 Submenu: LOOP")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            time.sleep(2)
            sub_choice = input("Enter your choice: ").lower()

            if sub_choice == 'a':
                # Definition
                print("\nLOOP: In programming, a loop is a control structure that repeats a block of code until a certain condition is met. Loops are fundamental for automating repetitive tasks and processing collections of data. Python supports both for loops (for iterating over sequences) and while loops (for repeating code as long as a condition is true).")
                time.sleep(2)
                input("\nPress Enter...")

            elif sub_choice == 'b':
                # Example (Fixed formatting)
                print("Input:")
                
                
                print("def calculate_even_total(start_num, end_num):")
                print("    total = 0")
                print("    for num in range(start_num, end_num + 1):")
                print("        if num % 2 == 0:")
                print("            total += num")
                print('            print(f"Added even number: {num} | Current total: {total}")')
                print("    return total")
                print("final_total = calculate_even_total(1, 10)")
                print('print("\\n--- Final Result ---")')
                print('print(f"Total of all even numbers between 1 and 10: {final_total}")')

                
                print("\nOutput:")
                
                
                print("Added even number: 2 | Current total: 2")
                print("Added even number: 4 | Current total: 6")
                print("Added even number: 6 | Current total: 12")
                print("Added even number: 8 | Current total: 20")
                print("Added even number: 10 | Current total: 30")
                print("\n--- Final Result ---")
                print("Total of all even numbers between 1 and 10: 30")

                time.sleep(2)
                input("\nPress Enter to continue...")

            elif sub_choice == 'c':
                break
            else:
                print("Invalid choice.")
                time.sleep(2)

    elif choice == "F":
        while True:
            clear()
            print("\nOPTION 6 Submenu: LIST")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")
            time.sleep(2)
            sub_choice = input("Enter your choice: ").lower()

            if sub_choice == 'a':
                # Definition
                print("\nLIST: A list in Python is a versatile, ordered, and mutable (changeable) data structure used to store a collection of items. Lists are defined using square brackets [] and can contain elements of different data types, including numbers, strings, and even other lists. Lists support various operations like indexing, slicing, appending, and inserting elements.")
                time.sleep(2)
                input("\nPress Enter...")

            elif sub_choice == 'b':
                # Example (Fixed formatting)
                print("Input:")
                
                
                print('fruit_list = ["apple", "banana", "cherry"]')
                print('print(f"Original List: {fruit_list}")')
                print('fruit_list.append("date")')
                print('print(f"\\nAfter append(\'date\'): {fruit_list}")')
                print('fruit_list.insert(1, "blueberry")')
                print('print(f"After insert(1, \'blueberry\'): {fruit_list}")')
                print('fruit_list.remove("banana")')
                print('print(f"After remove(\'banana\'): {fruit_list}")')
                print('cherry_index = fruit_list.index("cherry")')
                print('print(f"\\nIndex of \'cherry\' in the list: {cherry_index}")')
                print('fruit_list.sort()')
                print('print(f"After sorting alphabetically: {fruit_list}")')
                print('fruit_list_copy = fruit_list.copy()')
                print('print(f"\\nCopied list: {fruit_list_copy}")')

                print("\nOutput:")
                
                
                print("Original List: ['apple', 'banana', 'cherry']")
                print("\nAfter append('date'): ['apple', 'banana', 'cherry', 'date']")
                print("After insert(1, 'blueberry'): ['apple', 'blueberry', 'banana', 'cherry', 'date']")
                print("After remove('banana'): ['apple', 'blueberry', 'cherry', 'date']")
                print("\nIndex of 'cherry' in the list: 2")
                print("After sorting alphabetically: ['apple', 'blueberry', 'cherry', 'date']")
                print("\nCopied list: ['apple', 'blueberry', 'cherry', 'date']")

                time.sleep(2)
                input("\nPress Enter to continue...")

            elif sub_choice == 'c':
                break
            else:
                print("Invalid choice.")
                time.sleep(2)

    elif choice == "G":
        while True:
            clear()
            print("\nOPTION 7 Submenu: INT FUNCTION")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            time.sleep(2)
            sub_choice = input("Enter your choice: ").lower()

            if sub_choice == 'a':
                # Definition
                print("\nINT FUNCTION: The int() function in Python is a built-in function that converts a value to an integer data type. It can convert numbers (including floating-point numbers) and strings to integers. When converting a floating-point number, it truncates the decimal part. When converting a string, the string must represent a valid integer literal.")
                time.sleep(2)
                input("\nPress Enter...")

            elif sub_choice == 'b':
                # Example (Fixed formatting and simulated execution flow)
                print("Input:")
                
                
                print('print("=== Python int() Function Example ===")')
                print("float_num = 7.99")
                print("converted_float = int(float_num)")
                print('print(f"1. Convert float {float_num} to int: {converted_float}")')
                print('numeric_string = "42"')
                print("converted_string = int(numeric_string)")
                print('print(f"2. Convert numeric string \'{numeric_string}\' to int: {converted_string}")')
                print("bool_true = True")
                print("bool_false = False")
                print("converted_true = int(bool_true)")
                print("converted_false = int(bool_false)")
                print('print(f"3. Convert boolean True to int: {converted_true}")')
                print('print(f"   Convert boolean False to int: {converted_false}")')
                print('binary_string = "1010"')
                print("converted_binary = int(binary_string, 2)")
                print('print(f"4. Convert binary string \'{binary_string}\' (base 2) to int: {converted_binary}")')
                print("calc_result = converted_string + converted_float")
                print('print("\\n--- Using converted integers ---")')
                print('print(f"Calculation: {converted_string} + {converted_float} = {calc_result}")')

                print("\nOutput:")
                
                
                print("=== Python int() Function Example ===")
                print("1. Convert float 7.99 to int: 7")
                print("2. Convert numeric string '42' to int: 42")
                print("3. Convert boolean True to int: 1")
                print("   Convert boolean False to int: 0")
                print("4. Convert binary string '1010' (base 2) to int: 10")
                print("\n--- Using converted integers ---")
                print("Calculation: 42 + 7 = 49")

                input("\nPress Enter to continue...")

            elif sub_choice == 'c':
                break
            else:
                print("Invalid choice.")
                time.sleep(2)

    elif choice == "H":
        while True:
            clear()
            print("\nOPTION 8 Submenu: STRING CONCATENATION")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            time.sleep(2)
            sub_choice = input("Enter your choice: ").lower()

            if sub_choice == 'a':
                # Definition
                print('\nSTRING CONCATENATION: In programming using Python, string concatenation is the process of combining two or more separate string values into a single, continuous string. The most basic way to do this is using the + operator: for example, combining the strings "Hello " and "World" with "Hello " + "World" results in the single string "Hello World". You can also concatenate strings using the += operator to add a string to an existing string variable (e.g., greeting = "Hello "; greeting += "World" will set greeting to "Hello World"), or use the str.join() method to concatenate multiple strings from an iterable (like a list) with a specified separator.')
                time.sleep(2)
                input("\nPress Enter...")

            elif sub_choice == 'b':
                # Example (Fixed formatting and input/output simulation)
                print("Input:")
                
                
                print('first_name = input("Enter your first name: ")')
                print('last_name = input("Enter your last name: ")')
                print('greeting_start = "Hi, "')
                print('closing = "! Welcome to the Python string demo."')
                print('full_name = first_name + " " + last_name')
                print('greeting_1 = greeting_start + full_name + closing')
                print('greeting_2 = greeting_start')
                print('greeting_2 += full_name')
                print('greeting_2 += closing')
                print('greeting_segments = [greeting_start, full_name, closing]')
                print('greeting_3 = "".join(greeting_segments)')
                print('print("\\nGreeting (Method 1):", greeting_1)')
                print('print("Greeting (Method 2):", greeting_2)')
                print('print("Greeting (Method 3):", greeting_3)')

                print("\nOutput:")
                
                
                print("Enter your first name: Luna")
                print("Enter your last name: Reyes")
                print("\nGreeting (Method 1): Hi, Luna Reyes! Welcome to the Python string demo.")
                print("Greeting (Method 2): Hi, Luna Reyes! Welcome to the Python string demo.")
                print("Greeting (Method 3): Hi, Luna Reyes! Welcome to the Python string demo.")

                time.sleep(2)
                input("\nPress Enter to continue...")

            elif sub_choice == 'c':
                break
            else:
                print("Invalid choice.")
                time.sleep(2)

    elif choice == "I":
        while True:
            clear()
            print("\nOPTION 9 Submenu: EQUATIONS")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            time.sleep(2)
            sub_choice = input("Enter your choice: ").lower()

            if sub_choice == 'a':
                # Definition
                print("\nEQUATION: In Python, an equation is a line of code that establishes a relationship (most often an equality) between values, variables, or expressions, using Python's supported operators. This can include assignment equations (using the = operator, which sets a variable to a value/expression, e.g., total = price * quantity ), or comparison equations (using operators like == , > , or < to check if a relationship is true/false, e.g., is_adult = age >= 18 ). Equations in Python can also combine arithmetic, logical, or string operations to define or evaluate a specific relationship.")
                time.sleep(2)
                input("\nPress Enter to continue...")

            elif sub_choice == 'b':
                # Example (Fixed formatting and input/output simulation)
                print("Input:")
                
                
                print("item_price = 29.99")
                print('quantity = int(input("Enter how many items you want to buy: "))')
                print("tax_rate = 0.08")
                print("subtotal = item_price * quantity")
                print("tax_amount = subtotal * tax_rate")
                print("total_cost = subtotal + tax_amount")
                print("is_large_order = quantity >= 5")
                print("is_affordable = total_cost <= 100")
                print('print(f"\\nOrder Details:")')
                print('print(f"Subtotal: ${subtotal:.2f}")')
                print('print(f"Tax: ${tax_amount:.2f}")')
                print('print(f"Total Cost: ${total_cost:.2f}")')
                print('print(f"\\nOrder Notes:")')
                print('print(f"Large order (5+ items): {is_large_order}")')
                print('print(f"Total is under $100: {is_affordable}")')

                print("\nOutput:")
                
                
                print("Enter how many items you want to buy: 3")
                print("\nOrder Details:")
                print("Subtotal: $89.97")
                print("Tax: $7.20")
                print("Total Cost: $97.17")
                print("\nOrder Notes:")
                print("Large order (5+ items): False")
                print("Total is under $100: True")

                time.sleep(2)
                input("\nPress Enter to continue...")

            elif sub_choice == 'c':
                break
            else:
                print("Invalid choice.")
                time.sleep(2)

    elif choice == "J":
        while True:
            clear()
            print("\nOPTION 10 Submenu: WHILE LOOP")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            time.sleep(2)
            sub_choice = input("Enter your choice: ").lower()

            if sub_choice == 'a':
                # Definition
                print("\nWHILE LOOP: In Python, a while loop is a control flow structure that repeatedly runs an indented block of code as long as a specified boolean condition evaluates to True . The condition is checked before each iteration of the loop: if the condition is True , the code block runs; if it becomes False , the loop stops, and the program moves to the code after the loop. Unlike a for loop (which iterates over a defined iterable), a while loop is used for repeated tasks where the number of iterations is not known in advance (such as waiting for user input to meet a requirement, or running until a calculated value reaches a target).")
                time.sleep(2)
                input("\nPress Enter to continue...")

            elif sub_choice == 'b':
                # Example (Fixed indentation and print statements)
                
                print("Input:")
                
                
                print("while True:")
                print('    target_input = input("Enter a positive whole number to count *to* (or type \'down\' to count *from* that number): ")')
                print('    if target_input.lower() == "down":')
                print('        countdown = True')
                print('        while True:')
                print('            countdown_start = input("Enter the positive whole number to start the countdown from: ")')
                print('            if countdown_start.isdigit() and int(countdown_start) > 0:')
                print('                target = int(countdown_start)')
                print('                break')
                print('            else:')
                print('                print("Please enter a valid positive whole number.")')
                print('        break')
                print('    elif target_input.isdigit() and int(target_input) > 0:')
                print('        countdown = False')
                print('        target = int(target_input)')
                print('        break')
                print('    else:')
                print('        print("Please enter a valid positive whole number, or \'down\'.")')
                print('if not countdown:')
                print('    current_count = 1')
                print('    print(f"\\nCounting up to {target}:")')
                print('    while current_count <= target:')
                print('        print(current_count)')
                print('        current_count += 1')
                print('else:')
                print('    current_count = target')
                print('    print(f"\\nCounting down from {target}:")')
                print('    while current_count >= 1:')
                print('        print(current_count)')
                print('        current_count -= 1')
                print('print("\\nCount complete!")')

                print("\nOutput:")
                
                
                print("Enter a positive whole number to count *to* (or type 'down' to count *from* that number): 4")
                print("\nCounting up to 4:")
                print("1")
                print("2")
                print("3")
                print("4")
                print("\nCount complete!")

                time.sleep(2)
                input("\nPress Enter to continue...")

            elif sub_choice == 'c':
                break
            else:
                print("Invalid choice.")
                time.sleep(2)

    elif choice == "K":
        while True:
            clear()
            print("\nOPTION 11 Submenu: IF STATEMENT")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            time.sleep(2)
            sub_choice = input("Enter your choice: ").lower()

            if sub_choice == 'a':
                # Definition
                print("\nIF STATEMENT: In Python, if statement is a core control flow structure that runs a block of code only if a specified boolean condition evaluates to True . The condition is a statement that resolves to either True or False (using comparison operators like == , > , or logical operators like and / or ), and the indented code block under the if line will execute only when that condition is met; if the condition is False , the code block is skipped. You can also extend it with elif (else if) to check additional conditions, or else to run code when none of the prior conditions are true.")
                time.sleep(2)
                input("\nPress Enter to continue...")

            elif sub_choice == 'b':
                # Example (Fixed indentation and print statements)
                
                print("Input:")
                
                
                print("user_age = int(input('Enter your age: '))")
                print("if user_age < 13:")
                print('    print("You\'re in the kid age group!")')
                print("elif 13 <= user_age < 18:")
                print('    print("You\'re a teenager!")')
                print("elif 18 <= user_age < 65:")
                print('    print("You\'re an adult!")')
                print("else:")
                print('    print("You\'re in the senior age group!")')

                print("\nOutput:")
                
                
                print("Enter your age: 25")
                print("You're an adult!")

                time.sleep(2)
                input("\nPress Enter to continue...")

            elif sub_choice == 'c':
                break
            else:
                print("Invalid choice.")
                time.sleep(2)

    elif choice == "L":
        while True:
            clear()
            print("\nOPTION 12 Submenu: NESTED FOR LOOP")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

            time.sleep(2)
            sub_choice = input("Enter your choice: ").lower()

            if sub_choice == 'a':
                # Definition
                print("\nNESTED FOR LOOP: In Python, a nested for loop is a control flow structure where one for loop (called the inner loop) is defined entirely inside the indented code block of another for loop (called the outer loop). The outer loop runs first: for each single iteration of the outer loop, the inner loop will run through all of its own iterations (completing its full cycle) before the outer loop moves to its next iteration. This is most commonly used to work with multi-dimensional data (like a list of lists, or a grid) — for example, iterating over each row (outer loop) of a 2D list, then iterating over each item (inner loop) in that row.")
                time.sleep(2)
                input("\nPress Enter to continue...")

            elif sub_choice == 'b':
                # Example (Fixed indentation and print statements)
                
                print("Input:")
                
                
                print("number_grid = [")
                print("    [1, 2, 3, 4],")
                print("    [5, 6, 7, 8],")
                print("    [9, 10, 11, 12]")
                print("]")
                print("total_sum = 0")
                print("for row in number_grid:")
                print('    print(f"Checking row: {row}")')
                print("    for number in row:")
                print("        total_sum += number")
                print('print(f"\\nTotal sum of all numbers in the grid: {total_sum}")')

                print("\nOutput:")
                
                
                print("Checking row: [1, 2, 3, 4]")
                print("Checking row: [5, 6, 7, 8]")
                print("Checking row: [9, 10, 11, 12]")
                print("\nTotal sum of all numbers in the grid: 78")

                time.sleep(2)
                input("\nPress Enter to continue...")

            elif sub_choice == 'c':
                break
            else:
                print("Invalid choice.")
                time.sleep(2)

    elif choice == "X":
        print("\nThank you for using JEV'S program!")
        break

    else:
        print("Invalid choice.")
        time.sleep(2)
