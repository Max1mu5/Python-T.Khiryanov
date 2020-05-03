n = int(input())
c = {}
m = 0
while n != 0:
	if c.get(n, 0) == 0:
		c[n] = 1
	else:
		c[n] += 1
	if n > m:
		m = n
	n = int(input())
print(c[m])