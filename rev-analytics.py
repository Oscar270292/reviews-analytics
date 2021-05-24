data = []
i = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		i += 1
		if i % 1000 == 0:
			print(i)
