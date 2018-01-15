import json
numbers = [2,3,4,5,6,7]

filename ='jsondump.txt'
with open(filename,'w') as fileobj:
	json.dump(numbers,fileobj)



with open(filename) as fileobj:
	number = json.load(fileobj)

