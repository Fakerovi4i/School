

while True:
	count_digit = 0
	sym_up = False
	password = input("Введите пароль: ")
	for i in password:
		if i.isupper():
			sym_up = True
		elif i.isdigit():
			count_digit += 1
	if count_digit >= 3 and sym_up and len(password) >= 8:
		print("Это надежный пароль!й")
		break
	else:
		print("Попробуйте еще раз!")