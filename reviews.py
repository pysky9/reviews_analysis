data = []
with open("reviews.txt", "r") as f :
	for line in f :
		data.append(line)
		# 每讀一千筆 印出
		# if len(data) % 1000 == 0 :
		# 	print(len(data))
print("檔案讀取完了", len(data), "筆資料")

# 算留言平均長度
# 更新code
sum_len = 0
for line in data :
	sum_len += len(line)
print(f'留言平均長度為{sum_len/len(data)}')