import json
import time

begin = 1960
end = 2016

time_span = range(begin, end)

with open('./data/term_list.json', 'r') as f:
	data = json.load(f)
	terms = data['L0'] + data['L1'] + data['L2'] + data['Test']

terms = list(set(terms))
print('#terms = %d'%len(terms))

topic_year_paper = {}

for term in terms:
	topic_year_paper[term] = {}
	for year in time_span:
		topic_year_paper[term][year] = 0

count = 0
paper_title = {}
paper_year = {}
papers = []
with open('../MAG_data/Papers.txt', 'r') as f:
	for line in f.readlines():
		if count % 100000 == 0:
			print(count)
		count += 1
		tmp = line.split('\t')
		paperID = tmp[0].strip()
		year = int(tmp[3].strip())
		title = tmp[2].strip().lower()
		paper_title[paperID] = title
		paper_year[paperID] = year
		papers.append((title, year))
print("#papers = %d"%count)


for i, term in enumerate(terms):
	num = 0
	words = term.lower().replace('–', ' ').replace('-', ' ').split()
	for paper in papers:
		title = paper[0]
		year = paper[1]
		count = True
		for word in words:
			if word not in title: 
				count = False
				break
		if count and year in time_span: 
			topic_year_paper[term][year] += 1
			num += 1

with open('./result/paper_dict.json', 'w') as f:
	json.dump(topic_year_paper, f)

