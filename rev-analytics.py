data = []
i = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		i += 1
		if i % 1000 == 0:
			print(i)
print('讀取完了，總共有', len(data), '筆資料')
b = 0
for d in data:
	b += len(d)
print('留言的平均長度為', b / 1000000)