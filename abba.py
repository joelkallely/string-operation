jkhuihidef abba_pattern(a,b):
	c=a+b
	c=c+(b+a)
	return c

a = raw_input("Enter a string")
b = raw_input("Enter another string")
str = abba_pattern(a,b)
print str
