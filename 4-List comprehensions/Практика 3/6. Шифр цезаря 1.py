def cezar_pass(text, shift):
	frase_list = [(alphabet[(alphabet.index(sym) + shift) % 33] if sym != " "
				   else " ") for sym in text]
	for i in frase_list:
		frase_cezar += i
	return frase_cezar

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
text = "это питон"
K = 3

text_cezar = cezar_pass(text, K)

print(text_cezar)