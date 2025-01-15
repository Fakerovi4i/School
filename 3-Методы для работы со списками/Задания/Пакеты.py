N = int(input("Введите количество пакетов: "))
pack = []
decode = []
bad_pack = 0
for i in range(N):
	print("\nПакет номер", i+1)
	for i_bit in range(4):
		print("Введите", i_bit+1, "бит:", end = " ")
		bit = int(input())
		pack.append(bit)
	if pack.count(-1) > 1:
		bad_pack += 1
		print("Ошибка пакета!")
	else:
		decode.extend(pack)
	pack = []

print("Полученное сообщение:", decode)
print("Количество ошибок в сообщении:", decode.count(-1))
print("Количество потерянных пакетов:", bad_pack)