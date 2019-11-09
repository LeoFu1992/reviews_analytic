data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 1000 == 0: #和1000求餘數
			print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')

print(len(data[0]))
print(len(data[1]))
print(len(data[999999]))

sum_len = 0
for i in data:
	sum_len = sum_len + len(i)

print(sum_len/1000000)

