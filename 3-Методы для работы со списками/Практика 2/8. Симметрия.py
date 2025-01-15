def is_palindrome(new_list):
	palindrome = []
	for i in range(len(palindrome_list)-1, -1, -1):
		palindrome.append(palindrome_list[i])
	if palindrome == palindrome_list:
		return True
	else:
		return False
num_list = [1, 2, 3, 4, 5]
palindrome_list = []
answer_list = []

for i in range(len(num_list)):
	for j in range(i, len(num_list)):
		palindrome_list.append(num_list[j])
	if is_palindrome(palindrome_list):
		for i_palindrome in range(i):
			answer_list.append(num_list[i_palindrome])
		answer_list.reverse()
		break
	palindrome_list = []

print("Последовательность:", num_list)
print("Нужно приписать чисел;", len(answer_list))
print("Сами числа:", answer_list)
