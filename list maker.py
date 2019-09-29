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
        print(list_1)
        break
    except ValueError:
        print('list length should be a numerical value. try again.')
