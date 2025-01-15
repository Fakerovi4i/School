N = int(input("Количество участников: "))
K = int(input("Сколько человек в команде: "))
members = []
num = 1
flag = False
if N % K == 0:
	flag = True
	for _ in range(N // K):
		members.append(list(range(num, num+K)))
		num += K
else:
	print(N, "участников, невозможно поделить на команды по", K, "человек!")

if flag:
	print("Общий список команд:", members)