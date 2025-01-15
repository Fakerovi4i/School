

students = {
1: {
'name': 'Bob',
'surname': 'Vazovski',
'age': 23,
'interests': ['biology', 'swimming']
},
2: {
'name': 'Rob',
'surname': 'Stepanov',
'age': 24,
'interests': ['math', 'computer games', 'running']
},
3: {
'name': 'Alexander',
'surname': 'Krug',
'age': 22,
'interests': ['languages', 'health food']
}
}
#1 Вариант решения
def func(dict):
	list_key = []
	list_inter = [] #Может можно сразу сождать множество без списка но надо придумать тогда, вместо extend
	count_sur = 0
	for i_key, i_value in dict.items():
		list_key.append((i_key, i_value["age"]))
		list_inter.extend(i_value['interests'])
		count_sur += len(i_value['surname'])
	return list_key, list_inter, count_sur

key_age, interest, count_surname = func(students)

print("\nСписок пар «ID студента — возраст»:", key_age)
print("\nПолный список интересов всех студентов:", set(interest))
print("\nОбщая длина всех фамилий студентов:", count_surname)

#2 Решение через comprihantions (но тут по факту 3 цикла вместо одного)

# key_age = [tuple((i, students[i]["age"])) for i in students]
# print("\nСписок пар «ID студента — возраст»:", key_age)
#
# interest = {j for i in students.values() for j in i["interests"]}
# print("\nПолный список интересов всех студентов:", interest)
#
# count_surname = 0
# for i in students.values():
# 	count_surname += len(i["surname"])
# print("\nОбщая длина всех фамилий студентов:", count_surname)
