import os

path_to_file = os.path.abspath(os.path.join('..', 'farm-001.JPG'))

print("Путь:", path_to_file)

if not os.path.exists(path_to_file):
	print("Указанного пути не существует.")
elif os.path.isfile(path_to_file):
	print('Это файл размером:', os.path.getsize(path_to_file))
elif os.path.isdir(path_to_file):
	print('Это директория.')
elif os.path.islink(path_to_file):
	print('Это ссылка.')