N = int(input("Количество сотрудников: "))
salary_list = []

for emp in range(N):
	print(f"Введите зарплату {emp+1} сотрудника:", end = " ")
	sal = int(input())
	salary_list.append(sal)
for i in salary_list:
	if i == 0:
		salary_list.remove(0)

print("Осталось сотрудников:", len(salary_list))
print("Зарплаты:", salary_list)
print("Максимальная зарплата:", max(salary_list))
print("Минимальная зарплата:", min(salary_list))