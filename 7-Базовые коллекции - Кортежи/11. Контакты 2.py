kontacts_book = dict()
while True:
	print("Текущие контакты:")
	if not kontacts_book:
		print("Пусто")
	else:
		for i in kontacts_book:
			print("{0} {1}: {2}".format(i[0], i[1], kontacts_book[i]))
	name = tuple(input("\nВведите имя и фамилию через пробел: ").split())

	if name in kontacts_book:
		print("Ошибка: такое имя существует.")
		print()
		continue
	elif name[0] == "конец":
		for i in kontacts_book:
			print("{0} {1}: {2}".format(i[0], i[1], kontacts_book[i]))
		print("Завершение программы!")
		break
	kontacts_book[name] = input("Введите номер телефона: ")
	print()