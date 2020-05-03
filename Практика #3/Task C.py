x = int(input())
ans = 'NO'
if x % 4 == 0 and x % 100 != 0:
	ans = 'YES'
if x % 400 == 0:
	ans = 'YES'
	
print(ans)