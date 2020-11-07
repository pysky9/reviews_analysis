import time
data = []
with open("reviews.txt", "r") as f :
	for line in f :
		data.append(line)
		# 每讀一千筆 印出
		if len(data) % 1000 == 0 :
			print(len(data))
print("檔案讀取完了", len(data), "筆資料")

# 算留言平均長度
# 更新code
sum_len = 0
for line in data :
	sum_len += len(line)
print(f'留言平均長度為{sum_len/len(data)}')

# 算留言最長 & 印出
data_max = []
for line in data :
	data_max.append(len(line))
max_num = max(data_max)
print(max_num)
print(data[data_max.index(max_num)])

# 篩選留言字數少於100字
data_filter = []
for line in data:
	if len(line) < 100 :
		data_filter.append(line)
print(f"一共有{len(data_filter)}筆資料留言少於100字")

# 篩選留言有 good 單字
good = []
for d in data :
	if 'good' in d:
		good.append(d)
print(f"一共有{len(good)}筆留言提到GOOD")

# 讓使用者查詢
start_time = time.time()
wc = {} # word count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else :
			wc[word] = 1
end_time = time.time() 
run_time = end_time - start_time
print("運算時間為", run_time, "秒")

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
while True:
	word = input("請輸入查詢的字:")
	print("你查詢的", word, "出現", wc[word], "次")
	q = input("請問您還要查詢嗎(y/n):")
	if q.lower() == "n":
		print("謝謝你的查詢")
		break