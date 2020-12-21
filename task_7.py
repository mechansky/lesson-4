from math import factorial


def fact(n):
    for element in range(1, user_input + 1):
        yield f'{element}! = {factorial(element)}'


user_input = int(input('Введите число, факториал которого вы хотите найти: '))
generator = fact(user_input)

for element in fact(user_input):
    print(element)

print(generator)

