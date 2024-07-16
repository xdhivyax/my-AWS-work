num=int(input("enter how many numbers you want in the array"))
arr=[]
for i in range(num):
	element=int(input())
	arr.append(element)
for i in arr:
	if i % 1 == 0 and i % i ==0:
		print(i)