guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]

while True:
	print("Сейчас на вечеринке", len(guests), "человек:", guests)
	guest_add = input("Гость пришел или ушел?: ")

	if guest_add == "пришел":
		name = input("Введите имя гостя: ")
		if len(guests) < 6:
			print("Привет,", name + "!")
			guests.append(name)
		else:
			print("Сорян,", name + ",", "но мест нет.")
	elif guest_add == "ушел":
		name = input("Введите имя гостя: ")
		print("Пока,", name + "!")
		guests.remove(name)
	elif guest_add == "пора спать":
		print("Вечеринка закончилась! Пора спать!")
		break