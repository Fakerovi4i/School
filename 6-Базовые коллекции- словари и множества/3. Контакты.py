kontacts_book = dict()
while True:
	print("Текущие контакты:")
	if not kontacts_book:
		print("Пусто")
	else:
		for i in kontacts_book:
			print(i, kontacts_book[i])
	name = input("\nВведите имя: ")
	if name in kontacts_book:
		print("Ошибка: такое имя существует.")
		print()
		continue
	elif name == "конец":
		for i in kontacts_book:
			print(i, kontacts_book[i])
			print("Завершение программы!")
		break
	kontacts_book[name] = input("Введите номер телефона: ")
	print()


