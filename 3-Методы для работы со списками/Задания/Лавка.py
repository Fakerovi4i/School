goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
print('Текущий ассортимент:', goods)

fruit_name = input("Название нового фрукта: ")
price = int(input("Введите стоимость: "))

goods.append([fruit_name, price])
print("Новый асортимент:", goods)

for i in goods:
	i[1] += i[1] * 8 / 100

print("Новый ассортимент с увел. ценой:", goods)
