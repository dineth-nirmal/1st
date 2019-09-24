def counter(d, l, s):
	for item in word:
		if item.isalpha():
			l += 1
		elif item.isdigit():
			d += 1
		elif item.isspace():
			s += 1
	return l, d, s


word = input('Word: ')                                              #fixed
out = counter(0, 0, 0)
print(f'letters: {out[0]}\ndigits: {out[1]}\nspaces: {out[2]}')
