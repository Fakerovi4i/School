file = open('E:\task\group_1.txt', 'read')
summa = 0
for i_line in file:
    info = i_line.split()
    summa += info[2]
file = open('E:\task\group_1.txt', 'read')
diff = 0
for i_line in file:
    info = i_line.split()
    diff -= info[2]
file_2 = open('E:\task\group_2.txt', 'read')
compose = 0
for i_line in file:
    info = i_line.split()
    compose *= info[2]
print(summa)
print(diff)
print(compose)
