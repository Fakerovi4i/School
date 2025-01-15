student_data = input(
	"Введите информацию о студенте через пробел\n"
	"(имя, фамилия, город, место учёбы, оценки): "
)
student_data_list = student_data.split()
stud_dict = dict()

stud_dict["Имя"] = student_data_list[0]
stud_dict["Фамилия"] = student_data_list[1]
stud_dict["Город"] = student_data_list[2]
stud_dict["Место учебы"] = student_data_list[3]
stud_dict["Оценки"] = []
for i in student_data_list[4:]:
	stud_dict["Оценки"].append(int(i))

for i in stud_dict:
	print(f"{i} - {stud_dict[i]}")