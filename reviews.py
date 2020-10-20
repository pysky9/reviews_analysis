data = []
with open("reviews.txt", "r") as f :
	for line in f :
		data.append(line)
		# 每讀一千筆 印出
		if len(data) % 1000 == 0 :
			print(len(data))
print(len(data))
print(data[0])
print("--------")