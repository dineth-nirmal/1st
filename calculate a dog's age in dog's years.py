try:
	human_years = int(input("your dog's age in human years: "))
	counter = 0
	dog_years = 0
	while counter < human_years:  # if we set this to <= the loop will run extra circle
		counter += 1
		if counter <= 2:
			dog_years += 10.5
		else:
			dog_years += 4
	print(f'age in dog years: {dog_years}')
except ValueError:
	print('age should be a number. invalid value')
