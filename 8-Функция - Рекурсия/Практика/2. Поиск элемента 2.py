site = {
'html': {
'head': {
'title': 'Мой сайт'
},
'body': {
'h2': 'Здесь будет мой заголовок',
'div': 'Тут, наверное, какой-то блок',
'p': 'А вот здесь новый абзац',
"new": {"test": "Мое значение для теста 4ой вложенности"}
}
}
}

def find_key(dict_1, key, deep=0):
	if key in dict_1:
		return dict_1[key]
	if deep == 1:
		return None

	for i_value in dict_1.values():
		if isinstance(i_value, dict):
			result = find_key(i_value, key, deep-1)
			if result:
				break
	else:
		result = None

	return result

what_key = input("Какой ключ найти?: ")
deep_need = input("Хотите задать глубину?(y/n): ").lower()

if deep_need == "y":
	deeping = int(input("Введите глубину вложености: "))
	print("Значение ключа:", find_key(site, what_key, deep=deeping))
elif deep_need == "n":
	print("Значение ключа:", find_key(site, what_key))