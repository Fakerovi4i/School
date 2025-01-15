incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

print("Доход от фруктов составил:", sum(incomes.values()))
for i in incomes:
    if incomes[i] == min(incomes.values()):
        min_i = i
        print("Самый маленький доход у:", min_i)

incomes.pop(min_i)
print(incomes)

