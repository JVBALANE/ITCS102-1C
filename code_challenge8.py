print("MULTIPLICATION TABLE MAKER")

while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

print(f"\nMultiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
