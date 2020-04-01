#created 9/09/2019
#author :samuvel
a= int(input("enter number of digits you want in series (minimum 2): "))
 #getting the number of digits
start = 0
dummy = 1
 
print("\nfibonacci series is:")
print(start, ",", dummy, end=", ")
 
for i in range(2, a):#using for loop to start and end till the nth number
	next = start + dummy
	print( next, end=", ")
 
	start = dummy
	dummy = next
	
