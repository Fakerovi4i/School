text = input("Введите текст: ").split()
max = 0
for i in text:
	if len(i) > max:
		max = len(i)
		max_word = i
	#elif len(i) == max:


print("Самое длинное слово:", max_word)
print("Длина этого слова:", max, "сим.")