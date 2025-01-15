def cezar_pass(text, shift):
	frase_list = [(alphabet[(alphabet.index(sym) + shift) % 33] if sym != " "
				   else " ") for sym in text]
	frase_cezar = "".join(frase_list)
	# for i in frase_list:
	# 	frase_cezar += i
	print(frase_list)
	return frase_cezar

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
text = "Это питон".lower()
K = 3

text_cezar = cezar_pass(text, K)

print(text_cezar)