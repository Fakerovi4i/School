prefix = ("@", "№", "$", "%", "^", "&", "*", "()")
suffix = (".txt", ".docx")
file = "example.docx"

if not file.endswith(suffix):
	print("Неверное расширение файла!!")
elif file.startswith(prefix):
	print("Ошибка: недопустимые символы!")
else:
	print("Файл назван верно!")