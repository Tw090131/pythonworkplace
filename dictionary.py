# -*- coding: utf-8 -*-  
user = {'name':'zzw','age':18,'school':'bd'}
for key,val in user.items():
	print(key+":"+str(val))      

mlist = ['1','2','3','4','1']

print(set(mlist))
for i in set(mlist):
	print(i)
print(list(set(mlist)))

message = input("please enter:")
print(message)