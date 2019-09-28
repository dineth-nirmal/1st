list_lim = int(input('length of list: '))
list_1 = []
counter = 0
while counter < list_lim:
    try:
        number = int(input(f'Number {counter + 1}: '))
        list_1.append(number)
        counter += 1
    except ValueError:
        print('list item should be a number')
print(list_1)
