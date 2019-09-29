import json

data = {"spam" : "foo", "parrot" : 42}
in_json = json.dumps(data) # Encode the data

#file_json = json.loads('./test_file.txt')

with open("./test_file.txt",'r') as load_f:
	load_dict = json.load(load_f)
	print(load_dict)
	#load_dict['smallberg'] = [8200,{1:[['Python',81],['shirt',300]]}]
	#print(load_dict)


print(in_json)
