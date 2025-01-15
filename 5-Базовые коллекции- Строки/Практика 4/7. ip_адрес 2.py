OK = False
while OK == False:
	OK = True
	ip_adress = input("Введите IP: ")
	ip_list = ip_adress.split(".")

	for i in range(len(ip_list)):
		if ip_list[i].count(",") > 0:
			print(ip_list[i], "Адрес — это четыре числа, разделённые точками.")
			OK = False
		elif not ip_list[i].isdigit():
			print(ip_list[i], "- это не число!")
			OK = False
		elif ip_list[i].isdigit() and int(ip_list[i]) > 255:
			print(ip_list[i], "- больше 255!")
			OK = False

if OK:
	print("ip-адрес соответствует!")

