import json
import time

begin = 1960
end = 2016

time_span = range(begin, end)

total_paper = {}

for year in time_span:
	total_paper[year] = 0

count = 0
with open('../MAG_data/Papers.txt', 'r') as f:
	for line in f.readlines():
		if count % 100000 == 0:
			print(count)
		count += 1
		tmp = line.split('\t')
		year = int(tmp[3].strip())
		if year in time_span: total_paper[year] += 1

with open('./result/total_paper_dict.json', 'w') as f:
	json.dump(total_paper, f)