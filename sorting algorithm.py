def making_list(no_items):
	n_list = []
	for i in range(no_items):
		item = int(input('Number: '))				# this input should be int
		n_list.append(item)
	return n_list


def sorting(n):
	for j in range(len(n) - 1):
		for i in range(len(n) - 1):
			if n[i] <= n[i + 1]:
				pass
			else:
				n[i], n[i + 1] = n[i + 1], n[i]
	return n


number_of_items = int(input('how many items you want to store: '))
n = making_list(number_of_items)
print(sorting(n))
