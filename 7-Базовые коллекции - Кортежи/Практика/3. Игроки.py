from operator import index

players = {
("Ivan", "Volkin"): (10, 5, 13),
("Bob", "Robbin"): (7, 5, 14),
("Rob", "Bobbin"): (12, 8, 2)
}
print([(i_i2ndex+i_value) for i_index, i_value in players.items()])