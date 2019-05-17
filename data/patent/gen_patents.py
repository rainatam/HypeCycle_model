import json
import pandas as pd

begin = 1960
end = 2016

time_span = range(begin, end)

with open('./data/term_list.json', 'r') as f:
	data = json.load(f)
	terms = data['L0'] + data['L1'] + data['L2']

print('#terms = %d'%len(terms))

topic_year_patent = {}
total_patents = {}

for term in terms:
	topic_year_patent[term] = {}

for year in time_span:
	print(year, '(%d~%d)'%(begin, end))
	df = pd.read_csv('../../patent_data/patent_%d'%year, error_bad_lines=False)
	total_patents[year] = 0
	for i, term in enumerate(terms):
		key = df['abstract'].str.contains('', case=False)
		words = term.lower().replace('–', ' ').replace('-', ' ').split()
		for word in words:
			word = word.replace('(', '').replace(')', '')
			try:
				key = key & df['abstract'].str.contains(word, case=False)
			except:
				print(i, year, term, word)
		try:
			topic_year_patent[term][year] = df[key].shape[0]
			print(year, i, words, topic_year_patent[term][year])
		except:
			print(year, i, words, '***')

with open('./result/patent_dict_%d.json'%begin, 'w') as f:
	json.dump(topic_year_patent, f)


