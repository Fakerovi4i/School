import os

packege = 'access'
file = 'admin.bat'

path_re = os.path.join('access', 'admin.bat')
abs_path = os.path.abspath(file)

print(path_re)
print(abs_path)