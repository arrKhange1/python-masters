import random;

N = 10

random_list = random.sample(range(1,100), N)
print('standard list', random_list)

reversed_random_list = random_list[::-1]
print('reversed list', reversed_random_list)