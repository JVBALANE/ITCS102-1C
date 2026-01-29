word = input("Enter a word: ") 

length = len(word) 
list = []
sum = 0

for a in range(1, length + 1, 1):
	addToList = input(f"Enter a number {a}: ")
	list.append(addToList)
	
	sum += int(addToList)
	

average = sum / length
print(list)
print(f"The length of the word is {length}")
print(f"The average of the number is {average}")

if length < average:
	print(f"The length of the word {word} is lesser than the average.")
elif length >= average:
	print(f"The length of the word {word} is greater than the average.")
