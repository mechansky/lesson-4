from itertools import count
from itertools import cycle

user_input_count = (int(input('введите число начала отсчета: ')))
user_input_count2 = (int(input('введите конечное число: ')))

print(f'числа, начиная с {user_input_count}, заканчивая {user_input_count2}:')
for element in count(user_input_count):
    if element > user_input_count2:
        break
    else:
        print(element)

i = 1
user_input_cycle = input('введите значения, которые будут повторяться трижды: ')
for element in cycle(user_input_cycle):
    if i > len(user_input_cycle) * 3:
        break
    print(element)
    i += 1

