def triangles():
	lines = 1
	tempt = [1]
	while True:
		save = [1]
		i = 1
		j = 1
		while i <= lines-2:
			num = tempt[i-1]+tempt[i]
			save.append(num)
			i += 1
		if lines >= 2:
			save.append(1)
		lines += 1
		tempt = save[:]
		yield save

f = triangles()
for x in range(1,10):
	print(next(f))
