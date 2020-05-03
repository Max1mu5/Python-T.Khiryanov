n = int(input())
c = 0
while n != 0:
	if n > c:
		c = n
	n = int(input())
print(c)