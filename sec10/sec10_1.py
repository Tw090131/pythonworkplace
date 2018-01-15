filename = 'aaa.txt'
with open(filename) as file_obj:
	# contents = file_obj.read()
	# print(contents)
	# print("\n")
	print(file_obj.readlines())
	# for line in file_obj:
	# 	print(line + "---")

flag = True
while(flag):
	message = input("please enter what you like?")
	if(message != 'quit'):
		with open("10-5.txt",'a+') as file_obj:
			file_obj.write(message+"\n")
	else:
		print("you quit")
		flag = False
