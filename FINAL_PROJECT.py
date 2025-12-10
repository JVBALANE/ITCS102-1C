import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(2)
clear()
print("HELLO, I'M JOHN VINCENT. THIS IS MY PYTHON CODE COMPILER SYSTEM")
time.sleep(2)
username = input("Enter your name: ")
use = input(f"Hi {username}, do you want to use the system? (yes/no): ").lower()

if use != 'yes':
    print("System exited.")
    time.sleep(2)
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
    print("\n=========================================================")
    print("  X - Exit")

	time.sleep(2)
	choice = input("Input your choice: ").upper()

    if choice == "A":
        while True:
            clear()
            print("\nOPTION 1 Submenu:")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

			time.sleep(2)
            sub_choice = input("Enter your choice: ").lower()

            if sub_choice == 'a':
                print("\nPRINT: As described previously, the print()  function is a built-in tool used to output data or text to a standard output location, typically the user's console.")
                print("It converts data to a string representation for display and, by default, adds a newline character at the end of the output.")
                time.sleep(2)
                input("\nPress Enter to continue...")

            elif sub_choice == 'b':
                print("Hello, welcome to Jev's Python print function demo!")
                name = "Vincent"
                age = 18
                print("Name:", name, "Age:", age)
                print("Hobbies:")
                print("Cycling","Basketball","Badminton")
                print("Favorite Fruits:")
                print("Apple", "Banana", "Grapes","Jackfruit",sep=" | ")
                
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
            print("\nOPTION 2 Submenu:")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

			time.sleep(2)
            sub_choice = input("Enter your choice: ").lower()

            if sub_choice == 'a':
                print("\nDICTIONARY: In Python, a dictionary is a built-in data structure that stores collections of key-value pairs. Each key within a dictionary must be unique and immutable (like a string or number), while the corresponding values can be any Python object. Dictionaries are defined using curly braces  {}  and provide efficient ways to look up, insert, or delete values based on their associated keys.")
                 time.sleep(2)
                 
                 input("\nPress Enter...")

            elif sub_choice == 'b':
                student = {
                    "name": "Alice",
                    "age": 20,
                    "major": "Computer Science"
                }

                # Accessing dictionary values
                print(f"Name: {student['name']}")
                print(f"Age: {student['age']}")
                print(f"Major: {student['major']}")

                # Modifying a dictionary
                student["age"] = 21  # Updating the age
                student["gpa"] = 3.8  # Adding a new key-value pair

                # Printing the updated dictionary
                print("\nUpdated student information:")
                print(student)

                # Deleting a key-value pair
                del student["major"]

                # Printing the dictionary after deletion
                print("\nStudent information after removing major:")
                print(student)

                # Using dictionary methods
                print("\nDictionary length:", len(student))  # Number of key-value pairs
                print("Keys:", student.keys())        # Get all keys
                print("Values:", student.values())      # Get all values
                print("Items:", student.items())        # Get all key-value pairs as tuples

                # Checking if a key exists
                if "name" in student:
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
            print("\nOPTION 3 Submenu:")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")
			
			time.sleep(2)
            sub_choice = input("Enter your choice: ").lower()

            if sub_choice == 'a':
                print("\nFOR LOOP: A  for  loop in Python is a control flow statement used to iterate over a sequence (like a list, tuple, or string) or other iterable objects. It allows you to execute a block of code repeatedly, once for each item in the sequence. The loop continues until all items in the sequence have been processed.")
                 time.sleep(2)
                 input("\nPress Enter...")

            elif sub_choice == 'b':
                test_scores = [82, 94, 77, 89, 91, 73]
                total_score = 0
                score_count = len(test_scores)

                for score in test_scores:
                    total_score += score
                    print(f"Added score {score} | Current total: {total_score}")

                average_score = total_score / score_count

                print("\n--- Final Results ---")
                print(f"Total of all test scores: {total_score}")
                print(f"Number of test scores: {score_count}")
                print(f"Average test score: {round(average_score, 2)}")
                
                time.sleep(2)
                input("\nPress Enter to continue...")  # <-- Added pause

            elif sub_choice == 'c':
                break
            else:
                print("Invalid choice.")
                time.sleep(2)

    elif choice == "D":
        while True:
            clear()
            print("\nOPTION 4 Submenu:")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")
			
			time.sleep(2)
            sub_choice = input("Enter your choice: ").lower()

            if sub_choice == 'a':
                print("\nEVAL FUNCTION: The  eval()  function in Python is a built-in function that evaluates a string as a Python expression. It parses the string and executes it as if it were Python code, returning the result of the expression. Because of the possibility of executing arbitrary code, using  eval()  with untrusted input can pose significant security risks.")
                
                time.sleep(2)
                input("\nPress Enter...")

            elif sub_choice == 'b':
                x = 12
                y = 4
                expr1 = "x + y"
                expr2 = "x * y - 8"
                expr3 = "(x // y) + (x % y)"
                expr4 = "x > y"

                print(f"Using variables: x = {x}, y = {y}\n")

                result1 = eval(expr1)
                result2 = eval(expr2)
                result3 = eval(expr3)
                result4 = eval(expr4)

                print(f"Result of {expr1}: {result1}")
                print(f"Result of {expr2}: {result2}")
                print(f"Result of {expr3}: {result3}")
                print(f"Result of {expr4}: {result4}")
                
                time.sleep(2)
                input("\nPress Enter to continue...")  # <-- Added pause

            elif sub_choice == 'c':
                break
            else:
                print("Invalid choice.")
                time.sleep(2)

    elif choice == "E":
        while True:
            clear()
            print("\nOPTION 5 Submenu:")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")
			
			time.sleep(2)
            sub_choice = input("Enter your choice: ").lower()

            if sub_choice == 'a':
                print("\nLOOP: In programming, a loop is a control structure that repeats a block of code until a certain condition is met. Loops are fundamental for automating repetitive tasks and processing collections of data. Python supports both  for  loops (for iterating over sequences) and  while  loops (for repeating code as long as a condition is true).")
                
                time.sleep(2)
                input("\nPress Enter...")

            elif sub_choice == 'b':
                def calculate_even_total(start_num, end_num):
                    total = 0
                    for num in range(start_num, end_num + 1):
                        if num % 2 == 0:
                            total += num
                            print(f"Added even number: {num} | Current total: {total}")
                    return total

                final_total = calculate_even_total(1, 10)
                print("\n--- Final Result ---")
                print(f"Total of all even numbers between 1 and 10: {final_total}")
                
                time.sleep(2)
                input("\nPress Enter to continue...")  # <-- Added pause

            elif sub_choice == 'c':
                break
            else:
                print("Invalid choice.")
                time.sleep(2)

    elif choice == "F":
        while True:
            clear()
            print("\nOPTION 6 Submenu:")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")
			time.sleep(2)
            sub_choice = input("Enter your choice: ").lower()

            if sub_choice == 'a':
                print("\nLIST: A list in Python is a versatile, ordered, and mutable (changeable) data structure used to store a collection of items. Lists are defined using square brackets  []  and can contain elements of different data types, including numbers, strings, and even other lists. Lists support various operations like indexing, slicing, appending, and inserting elements.")
                
                time.sleep(2)
                input("\nPress Enter...")

            elif sub_choice == 'b':
                fruit_list = ["apple", "banana", "cherry"]
                print(f"Original List: {fruit_list}")

                fruit_list.append("date")
                print(f"\nAfter append('date'): {fruit_list}")

                fruit_list.insert(1, "blueberry")
                print(f"After insert(1, 'blueberry'): {fruit_list}")

                fruit_list.remove("banana")
                print(f"After remove('banana'): {fruit_list}")

                cherry_index = fruit_list.index("cherry")
                print(f"\nIndex of 'cherry' in the list: {cherry_index}")

                fruit_list.sort()
                print(f"After sorting alphabetically: {fruit_list}")

                fruit_list_copy = fruit_list.copy()
                print(f"\nCopied list: {fruit_list_copy}")
                
                time.sleep(2)
                input("\nPress Enter to continue...")  # <-- Added pause

            elif sub_choice == 'c':
                break
            else:
                print("Invalid choice.")
                time.sleep(2)

    elif choice == "G":
        while True:
            clear()
            print("\nOPTION 7 Submenu:")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")
			
			time.sleep(2)
            sub_choice = input("Enter your choice: ").lower()

            if sub_choice == 'a':
                print("\nINT FUNCTION: The  int()  function in Python is a built-in function that converts a value to an integer data type. It can convert numbers (including floating-point numbers) and strings to integers. When converting a floating-point number, it truncates the decimal part. When converting a string, the string must represent a valid integer literal.")
                
                time.sleep(2)
                input("\nPress Enter...")

            elif sub_choice == 'b':
                print("=== Python int() Function Example ===")

                float_num = 7.99
                converted_float = int(float_num)
                print(f"1. Convert float {float_num} to int: {converted_float}")

                numeric_string = "42"
                converted_string = int(numeric_string)
                print(f"2. Convert numeric string '{numeric_string}' to int: {converted_string}")

                bool_true = True
                bool_false = False
                converted_true = int(bool_true)
                converted_false = int(bool_false)
                print(f"3. Convert boolean True to int: {converted_true}")
                print(f"   Convert boolean False to int: {converted_false}")

                binary_string = "1010"
                converted_binary = int(binary_string, 2)
                print(f"4. Convert binary string '{binary_string}' (base 2) to int: {converted_binary}")

                calc_result = converted_string + converted_float
                print("\n--- Using converted integers ---")
                print(f"Calculation: {converted_string} + {converted_float} = {calc_result}")
                input("\nPress Enter to continue...")  # <-- Added pause

            elif sub_choice == 'c':
                break
            else:
                print("Invalid choice.")
                time.sleep(2)

     elif choice == "H":
        while True:
            clear()
            print("\nOPTION 8 Submenu:")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")
			
			time.sleep(2)
            sub_choice = input("Enter your choice: ").lower()

            if sub_choice == 'a':
                print("\nSTRING CONCATENATION: In programming using Python, string concatenation is the process of combining two or more separate string values into a single, continuous string. The most basic way to do this is using the  +  operator: for example, combining the strings  "Hello "  and  "World"  with  "Hello " + "World"  results in the single string  "Hello World" . You can also concatenate strings using the  +=  operator to add a string to an existing string variable (e.g.,  greeting = "Hello "; greeting += "World"  will set  greeting  to  "Hello World" ), or use the  str.join()  method to concatenate multiple strings from an iterable (like a list) with a specified separator.")
                
                time.sleep(2)
                input("\nPress Enter...")

            elif sub_choice == 'b':
                def 
                # Define base string variables
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
greeting_start = "Hi, "
closing = "! Welcome to the Python string demo."

# Method 1: + operator (combine individual strings)
full_name = first_name + " " + last_name
greeting_1 = greeting_start + full_name + closing

# Method 2: += operator (add to an existing string variable)
greeting_2 = greeting_start
greeting_2 += full_name
greeting_2 += closing

# Method 3: str.join() (combine a list of string segments)
greeting_segments = [greeting_start, full_name, closing]
greeting_3 = "".join(greeting_segments)

# Print the results (all will be identical)
print("\nGreeting (Method 1):", greeting_1)
print("Greeting (Method 2):", greeting_2)
print("Greeting (Method 3):", greeting_3)
        
                time.sleep(2)
                input("\nPress Enter to continue...")  # <-- Added pause

            elif sub_choice == 'c':
                break
            else:
                print("Invalid choice.")
                time.sleep(2)
    
        elif choice == "I":
        while True:
            clear()
            print("\nOPTION 9 Submenu:")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

			time.sleep(2)
            sub_choice = input("Enter your choice: ").lower()

            if sub_choice == 'a':
                print("\nEQUATION: In Python, an equation is a line of code that establishes a relationship (most often an equality) between values, variables, or expressions, using Python's supported operators. This can include assignment equations (using the  =  operator, which sets a variable to a value/expression, e.g.,  total = price * quantity ), or comparison equations (using operators like  == ,  > , or  <  to check if a relationship is true/false, e.g.,  is_adult = age >= 18 ). Equations in Python can also combine arithmetic, logical, or string operations to define or evaluate a specific relationship.")
                
                time.sleep(2)
                input("\nPress Enter to continue...")

            elif sub_choice == 'b':
# Assignment equations: set values / calculate totals
item_price = 29.99
quantity = int(input("Enter how many items you want to buy: "))
tax_rate = 0.08  # 8% tax
subtotal = item_price * quantity
tax_amount = subtotal * tax_rate
total_cost = subtotal + tax_amount

# Comparison equations: check conditions
is_large_order = quantity >= 5  # True if 5+ items, False otherwise
is_affordable = total_cost <= 100  # True if total is $100 or less

# Print results
print(f"\nOrder Details:")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax_amount:.2f}")
print(f"Total Cost: ${total_cost:.2f}")
print(f"\nOrder Notes:")
print(f"Large order (5+ items): {is_large_order}")
print(f"Total is under $100: {is_affordable}")

				 time.sleep(2)
                input("\nPress Enter to continue...")  # <-- Added pause
                
            elif sub_choice == 'c':
                break
            else:
                print("Invalid choice.")
                time.sleep(2)
          
            
            elif choice == "J":
        while True:
            clear()
            print("\nOPTION 10 Submenu:")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

			time.sleep(2)
            sub_choice = input("Enter your choice: ").lower()

            if sub_choice == 'a':
                print("\nWHILE LOOP: In Python, a  while  loop is a control flow structure that repeatedly runs an indented block of code as long as a specified boolean condition evaluates to  True . The condition is checked before each iteration of the loop: if the condition is  True , the code block runs; if it becomes  False , the loop stops, and the program moves to the code after the loop. Unlike a  for  loop (which iterates over a defined iterable), a  while  loop is used for repeated tasks where the number of iterations is not known in advance (such as waiting for user input to meet a requirement, or running until a calculated value reaches a target).")
                
                time.sleep(2)
                input("\nPress Enter to continue...")

            elif sub_choice == 'b':
            	# First, get a valid positive target number (using a while loop for input validation)
while True:
    target_input = input("Enter a positive whole number to count *to* (or type 'down' to count *from* that number): ")
    # Check if user wants a countdown
    if target_input.lower() == "down":
        countdown = True
        # Get the starting number for the countdown
        while True:
            countdown_start = input("Enter the positive whole number to start the countdown from: ")
            if countdown_start.isdigit() and int(countdown_start) > 0:
                target = int(countdown_start)
                break
            else:
                print("Please enter a valid positive whole number.")
        break
    # Check if the input is a valid positive number for counting up
    elif target_input.isdigit() and int(target_input) > 0:
        countdown = False
        target = int(target_input)
        break
    else:
        print("Please enter a valid positive whole number, or 'down'.")

# Set up the counter based on count up / countdown
if not countdown:
    current_count = 1
    # While loop for counting UP
    print(f"\nCounting up to {target}:")
    while current_count <= target:
        print(current_count)
        current_count += 1
else:
    current_count = target
    # While loop for counting DOWN
    print(f"\nCounting down from {target}:")
    while current_count >= 1:
        print(current_count)
        current_count -= 1

print("\nCount complete!")

				 time.sleep(2)
                input("\nPress Enter to continue...")  # <-- Added pause
                
            elif sub_choice == 'c':
                break
            else:
                print("Invalid choice.")
                time.sleep(2)
    
            elif choice == "K":
        while True:
            clear()
            print("\nOPTION 11 Submenu:")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

			time.sleep(2)
            sub_choice = input("Enter your choice: ").lower()

            if sub_choice == 'a':
                print("\nIF STATEMENT: In Python, if statement is a core control flow structure that runs a block of code only if a specified boolean condition evaluates to  True . The condition is a statement that resolves to either  True  or  False  (using comparison operators like  == ,  > , or logical operators like  and / or ), and the indented code block under the  if  line will execute only when that condition is met; if the condition is  False , the code block is skipped. You can also extend it with  elif  (else if) to check additional conditions, or  else  to run code when none of the prior conditions are true.")
                
                time.sleep(2)
                input("\nPress Enter to continue...")

            elif sub_choice == 'b':
            	# Get user input
user_age = int(input("Enter your age: "))

# If/elif/else condition chain
if user_age < 13:
    print("You're in the kid age group!")
elif 13 <= user_age < 18:
    print("You're a teenager!")
elif 18 <= user_age < 65:
    print("You're an adult!")
else:
    print("You're in the senoir age group!!.")
            	
				 time.sleep(2)
                input("\nPress Enter to continue...")  # <-- Added pause
                
            elif sub_choice == 'c':
                break
            else:
                print("Invalid choice.")
                time.sleep(2)
    
    elif choice == "L":
        while True:
            clear()
            print("\nOPTION 12 Submenu:")
            print("a - Definition")
            print("b - Example")
            print("c - Back to Main Menu")

			time.sleep(2)
            sub_choice = input("Enter your choice: ").lower()

            if sub_choice == 'a':
                print("\nNESTED FOR LOOP: In Python, a nested for loop is a control flow structure where one  for  loop (called the inner loop) is defined entirely inside the indented code block of another  for  loop (called the outer loop). The outer loop runs first: for each single iteration of the outer loop, the inner loop will run through all of its own iterations (completing its full cycle) before the outer loop moves to its next iteration. This is most commonly used to work with multi-dimensional data (like a list of lists, or a grid) — for example, iterating over each row (outer loop) of a 2D list, then iterating over each item (inner loop) in that row.")
                
                time.sleep(2)
                input("\nPress Enter to continue...")

            elif sub_choice == 'b':
            # Define a 2D list (grid: 3 rows, 4 columns of numbers)
number_grid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

total_sum = 0

# Outer for loop: iterate over EACH ROW in the grid
for row in number_grid:
    # Print the current row (for clarity)
    print(f"Checking row: {row}")
    # Inner for loop: iterate over EACH NUMBER in the current row
    for number in row:
        # Add the current number to the total sum
        total_sum += number

# Print the final total
print(f"\nTotal sum of all numbers in the grid: {total_sum}")

				 time.sleep(2)
                input("\nPress Enter to continue...")  # <-- Added pause
                
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
