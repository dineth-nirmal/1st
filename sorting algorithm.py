def list_maker():    
    while True:
        try:
            list_len = int(input('list length: '))
            list_1 = []
            counter = 0
            while counter < list_len:
                try:
                    item_input = int(input(f'Number ({counter + 1}): '))
                    list_1.append(item_input)
                    counter += 1
                except ValueError:
                    print('invalid value')
            return list_1
        except ValueError:
            print('list length should be a numerical value. try again.')


def sorting(list_1):
    for j in range(len(list_1) - 1):
        for i in range(len(list_1) - 1):
            if list_1[i] < list_1[i + 1]:
                pass
            else:
                list_1[i], list_1[i + 1] = list_1[i + 1], list_1[i]
    return list_1


print(sorting(list_maker()))
