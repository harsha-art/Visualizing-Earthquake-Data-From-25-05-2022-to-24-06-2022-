import json 

filename = 'data/all_month.json'
with open(filename, encoding="utf8") as f:
	read = json.load(f)
print(read)

read_file = 'data/readable_all_month.json'
with open(read_file,'w') as f:
	json.dump(read,f,indent = 4)


