import random


d = {f'key{i}': random.choice([random.randint(1, 10), round(random.uniform(1, 20), 2)]) for i in range(1, 6)}

print('original dict:', d)

item_to_keys = dict()
for (key, item) in d.items():
    if (item, type(item)) in item_to_keys:
        item_to_keys[(item, type(item))].append(key)
    else:
        item_to_keys[(item, type(item))] = [key]

result_list = []
for item_type_tuple, key_list in item_to_keys.items():
    result_list.append((item_type_tuple[0], key_list)) # item_type_tuple = (1,2, float)

print('result list:', result_list)

