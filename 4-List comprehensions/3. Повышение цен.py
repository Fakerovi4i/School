def up_price(precent, i_price):
	return i_price * (1 + precent / 100)

price = [1.09, 23.56, 57.84, 4.56, 6.78]
x = 0
y = 10

first_year = [up_price(x, i_first) for i_first in price]
second_year = [up_price(y, i_second) for i_second in price]

print("Сумма цен за два года:", sum(price), round(sum(first_year), 2), round(sum(second_year), 2))