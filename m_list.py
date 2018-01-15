
mlist = ['aaaaa','bbbbb','cccccc']
mlist.append("lall")
mlist.insert(2,'ddddd')
print(mlist)

for key in mlist:
	print(key)

mlist = range(1,100)
for val in mlist:
	print(val)

mlist = list(mlist)
print(sum(mlist))

square = [value ** 2 for value in range(1,11)]
print(square)