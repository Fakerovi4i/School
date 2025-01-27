import os

path_to_project = os.path.abspath(os.path.join('..', '..', 'pythonProject1'))

print("Содержимое папки (pythonProject1):")
for i_elem in os.listdir(path_to_project):
	path_elem = os.path.join(path_to_project, i_elem)
	print('    ', path_elem)