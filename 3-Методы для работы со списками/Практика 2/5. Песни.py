violator_songs = [
['World in My Eyes', 4.86],
['Sweetest Perfection', 4.43],
['Personal Jesus', 4.56],
['Halo', 4.9],
['Waiting for the Night', 6.07],
['Enjoy the Silence', 4.20],
['Policy of Truth', 4.76],
['Blue Dress', 4.29],
['Clean', 5.83]
]

N = int(input("Сколько песен выбрать: "))
summ = 0

for i in range(1, N+1):
	print(f"Введите название {i}-ой песни:", end = " " )
	song = input()
	for ii in violator_songs:
		if ii[0] == song:
			summ += ii[1]

print("Общее время звучания:", round(summ, 2), "минут")