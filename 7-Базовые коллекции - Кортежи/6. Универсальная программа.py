def univers(data_iter):
	txt_honest_i = []
	for in_x, sym in enumerate(data_iter):
		if in_x % 2 == 0:
			txt_honest_i.append(sym)
	return txt_honest_i

text = [100, 200, 300, 'буква', 0, 2, 'а']

if isinstance(text, (str, tuple, list, dict)):
	print("Результат:", univers(text))
else:
	print("Тип данных не итерируется!")