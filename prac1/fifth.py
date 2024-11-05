import random


d1 = {f'key{i}': random.choice([random.randint(1, 100), round(random.uniform(1, 25), 2)]) for i in range(1, 6)}
d2 = {f'key{i}': random.choice([random.randint(1, 100), round(random.uniform(1, 25), 2)]) for i in range(1, 6)}

print('d1:', d1, '\nd2:', d2)

intersection_values = set(d1.values()) & set(d2.values())

concat_dicts = [*d1.items(), *d2.items()]
d3 = {}

for k, v in concat_dicts:
    if v in intersection_values:
        d3[k] = v

print('result:', d3)
