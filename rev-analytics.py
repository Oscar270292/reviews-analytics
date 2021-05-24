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
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('共有', len(new), '筆資料長度小於100')
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good),'筆資料提到good' )
print(good[2])

disappointed = [d for d in data if 'disappointed' in d]
print(len(d))
print(disappointed[766])
