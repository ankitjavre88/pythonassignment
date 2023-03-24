a=int(input("Enter valid Number"))
b=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
if 1<= a <=7:
	a-=1
	print(b[a])
else:
	print("Invalid")	