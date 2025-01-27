import os

def find_file(cur_path, file, path_list=[]):
	print("Переходим в:", cur_path)

	for i_elem in os.listdir(cur_path):
		path = os.path.join(cur_path, i_elem)
		print('     ',"Смотрим в:", path)
		if file == i_elem:
			path_list.append(path)
		if os.path.isdir(path):
			print('     ', "Это директория.")
			find_file(path, file)

	return path_list

print("Ищем в:", os.path.abspath('..'))
file_name = 'test.py'

path_list = find_file(os.path.abspath('..'), file_name)
if path_list:
	print("\nНайдены следующие пути: ")
	for i_file_path in path_list:
		print('     ', i_file_path)
else:
	print("Ни один файл не найден.")


