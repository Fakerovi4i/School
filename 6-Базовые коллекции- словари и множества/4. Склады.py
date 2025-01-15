small_storage = {
	'гвозди': 5000,
	'шурупы': 3040,
	'саморезы': 2000
}
big_storage = {
	'доски': 1000,
	'балки': 150,
	'рейки': 600
}
big_storage.update(small_storage)

while True:
	item = input("Каокой товар ищите?: ")
	if item in big_storage:
		print(item, "-", big_storage.get(item))
	elif item == "стоп":
		print("Завершение программы.")
		break
	else:
		print("Ошибка: такого значения нет.")

