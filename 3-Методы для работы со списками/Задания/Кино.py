def film_exist(films, add):
	for i_film in films:
		if i_film == add:
			return True
	return False

films = [
	'Крепкий орешек', 'Назад в будущее', 'Таксист',
	'Леон', 'Богемская рапсодия', 'Город грехов',
	'Мементо', 'Отступники', 'Деревня',
	'Проклятый остров', 'Начало', 'Матрица'
]
top_list = ['Отступники', 'Деревня',
	'Проклятый остров', 'Начало']

while True:
	print("Ваше изранное:", top_list)
	add_film = input("Введите название фильма?: ")
	command = input("Что сделать (добавить, поменять, удалить)?: ")
	if command == 'добавить':
		if film_exist(films, add_film) and (film_exist(top_list, add_film) == False):
			top_list.append(add_film)
		elif film_exist(films, add_film) == False:
			print("Такого фильма у нас нет!")
		elif film_exist(top_list, add_film):
			print("Фильм уже в избранном!")
	if command == "поменять":
		if film_exist(top_list, add_film):
			top_list.remove(add_film)
			que = int(input("На какое место: "))
			top_list.insert(que - 1, add_film)
		else:
			print("Такого фильма нет в избранном!")
	if command == "удалить":
		if film_exist(top_list, add_film):
			top_list.remove(add_film)
		else:
			print("Такого фильма нет в избранном!")



