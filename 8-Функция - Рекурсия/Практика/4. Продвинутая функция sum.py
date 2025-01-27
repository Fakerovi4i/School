def sum(*args, total=0):
	for i_data in args:
		if isinstance(i_data, int):
			total += i_data
		elif isinstance(i_data, (list, tuple)):
			total += sum(*i_data)
	return total

print(sum([[1, 2, [3]], [1], 3]))
#Ответ в консоли: 10
print(sum(1, 2, 3, 4, 5))
#Ответ в консоли: 15