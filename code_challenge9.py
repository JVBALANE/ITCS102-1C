import time

print("COUNTDOWN TIMER SIMULATOR")

while True:
    try:
        start_number = int(input("Enter the starting number for countdown: "))
        if start_number <= 0:
            print("Please enter a positive number for the countdown.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("\nCountdown started:")
for i in range(start_number, 0, -1):
    print(i)
    time.sleep(1) # Optional: Adds a 1-second delay for a more realistic countdown effect

print("Liftoff!")
