def sorting(n):
	for j in range(len(n) - 1):
		for i in range(len(n) - 1):
			if n[i] <= n[i + 1]:
				pass
			else:
				n[i], n[i + 1] = n[i + 1], n[i]
	return n


n = [7, 4, 2]
print(sorting(n))
