data = {(5000, 123456): ('Иванов', 'Василий'),
		(6000, 111111): ('Иванов', 'Петр'),
		(7000, 222222): ('Медведев', 'Алексей'),
		(8000, 333333): ('Алексеев', 'Георгий'),
		(9000, 444444): ('Георгиева', 'Мария')}

pas_n = int(input("Номер паспорта: "))
pas_ser = int(input("Серия: "))

print(data[(pas_n, pas_ser)])