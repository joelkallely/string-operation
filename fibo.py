num = int(input( "Enter the limit:"))
print num
a,b = 1,1 
print a
for i in range(num):
	a,b =b, a+b
        print a
