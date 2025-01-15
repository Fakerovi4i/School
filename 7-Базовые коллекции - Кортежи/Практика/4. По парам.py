import random
original_list = [random.randint(1, 100) for _ in range(10)]

#new_list = [(original_list[i], original_list[i+1]) for i in range(0, 10, 2)]

new_list = [tuple(original_list[i:i+2]) for i in range(0, len(original_list), 2)]

print(original_list)
print(new_list)