data = []
with open("reviews.txt", "r") as f :
	for line in f :
		data.append(line)
		# 每讀一千筆 印出
		if len(data) % 1000 == 0 :
			print(len(data))
print("檔案讀取完了", len(data), "筆資料")

# 算留言平均長度
data_length = []
with open("reviews.txt", "r") as f :
	for line in f :
		data_length.append(len(line))
avr_reviews = sum(data_length) / len(data_length)
print(f"留言平均長度為{avr_reviews}")