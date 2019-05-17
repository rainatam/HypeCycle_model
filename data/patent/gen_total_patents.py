import json
import pandas as pd

df = pd.read_csv('../patent.tsv', sep='\t', error_bad_lines=False)

print('# of lines = %d'%df.size)

start = 1960
end = 2016
time_span = [i for i in range(start, end)]

total_patent = {}
for year in time_span:
	print(year)
	selected_df = df.loc[(df['date'] >= '%d-01-01'%year) & (df['date'] <= '%d-12-31'%year)]
	print('# of lines = %d'%selected_df.size)
	total_patent[year] = int(selected_df.size)
	# selected_df.to_csv('../patent_data/patent_%d.csv'%year)

print(total_patent)
with open('./data/total_patent_dict.json', 'w') as f:
	json.dump(total_patent, f)