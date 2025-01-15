sinonim_dict = dict()
quant = int(input("Введите количество пар: "))

for i in range(quant):
	print("{0}-ая пара: ".format(i+1))
	sinonim_sinonim = input()
	sinonim_sinonim = sinonim_sinonim.split(" - ")
	sinonim_dict[sinonim_sinonim[0]] = sinonim_sinonim[1]

print(sinonim_dict)

while True:
	flag = False
	find = input("Введите слово: ").lower()
	for i_values in sinonim_dict:
		if find.lower() == i_values.lower():
			print("Синоним:", sinonim_dict[find])
			flag = True
		elif find == (sinonim_dict[i_values]).lower():
			print("Синоним:", i_values)
			flag = True
	if flag == False:
		print("Такого слова в словаре нет.")
	else:
		break

