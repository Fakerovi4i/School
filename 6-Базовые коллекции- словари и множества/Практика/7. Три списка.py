array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

new_array_first = []
new_array_second = []

#1.	найти элементы, которые есть в каждом списке;
for i in array_1:
	if i in array_2 and i in array_3:
		new_array_first.append(i)

new_array_first = ", ".join([str(i) for i in new_array_first])
print("Задача 1.")
print("Без использования множеств:", new_array_first)

set_intersection = set(array_1) & set(array_2) & set(array_3)
print("С использованием множеств:", ", ".join([str(i) for i in set_intersection]))

#2.	найти элементы из первого списка, которых нет во втором и третьем списках.
for i in array_1:
	if not i in array_2 and not i in array_3:
		new_array_second.append(i)

new_array_second = ", ".join([str(i) for i in new_array_second])
print("\nЗадача 2.")
print("Без использования множеств:", new_array_second)

set_intersection_2 = set(array_1) - set(array_2) - set(array_3)
print("С использованием множеств:", ", ".join([str(i) for i in set_intersection_2]))

