# input list elements
l = []
for i in input().split():
	l.append(int(i))
even_nums = []
for i in range(len(l)):
	if l[i]%2 == 0:
		even_nums.append(l[i])
print('Even nums => ',even_nums)
