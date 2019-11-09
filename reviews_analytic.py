data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 1000 == 0: #和1000求餘數
			print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')


sum_len = 0
for i in data:
	sum_len = sum_len + len(i)
print(sum_len/len(data))

new = [] #如果留言字串數小於 100 則拉出來
for i in data:
	if len(i) < 100:
		new.append(i)
print('一共有', len(new), '筆資料')

good = [] #如果留言字串出現 good 則拉出來
for i in data:
	if 'good' in i:
		good.append(i)
print('一共有', len(good), '筆資料')