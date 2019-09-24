input_word = input('Message: ').replace(' ','')
ints = 0
strs = 0
for letter in input_word:
    try:
        int(letter)
        ints += 1
    except ValueError:
        strs += 1
print(f'letters = {strs}')
print(f'numbers = {ints}')
