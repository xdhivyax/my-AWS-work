a=int(input("Enter the a value :"))
b=int(input("Enter the b value :"))
c=int(input("Enter the c value :"))
if (a>=b and a>=c):
	print(f"{a} is greater")
elif (b>=a and b>=c):
    print(f"{b} is greater")
else:
	print(f"{c} is greater")