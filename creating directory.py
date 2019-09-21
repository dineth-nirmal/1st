def storing(name, age):
    customers[name] = age


customers = {

}
counter = 0
maximum_limit = 10
while counter < maximum_limit:
    name_in = input('Name: ')
    if name_in == 'print':
        break
    age_in = input('age: ')
    storing(name_in, age_in)
    counter += 1
print(customers)
