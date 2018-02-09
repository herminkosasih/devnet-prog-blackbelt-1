import random

if __name__ == '__main__':

	User_Input = 0

	while True:
		try:
			User_Input = int(input("Guess the number: "))
		except ValueError:
			print("Not an integer!\n")
			continue
		else:
			random_value = random.randint(0,10)
			if random_value == User_Input:
				print ("Correct!\n")
				break
			else:
				print ("Wrong, try again!\n")
