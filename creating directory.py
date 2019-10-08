d_length = int(input('dictionary length: '))
list_d = {}
counter = 0
while counter < d_length:
    try:
        key_d = int(input('key: ').replace(' ', ''))
        value_d = int(input('value: ').replace(' ', ''))
        if key_d in list_d:
            print('That key is already in the dictionary')
            y_or_n = input('Do you want to overwrite it,(yes or no) : ').lower()
            while True:
                if y_or_n == 'yes':
                    list_d[key_d] = value_d
                    break
                elif y_or_n == 'no':
                    break
                else:
                    print('invalid value')
        else:
            list_d[key_d] = value_d
            counter += 1
    except ValueError:
        print('invalid values')
print(list_d)
