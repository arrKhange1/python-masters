import random

first_list = random.sample(range(1,100), 4)
second_list = random.sample(range(1,100), 3)
third_list = [*first_list[::2], *second_list[1::2]]

print('first list:', first_list, 'second_list:', second_list)
print('third list:', third_list)

