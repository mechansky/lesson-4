from functools import reduce


def multiplication(prev_element, element):
    return int(prev_element * element)


result_list = [element for element in range(100, 1001) if element % 2 == 0]
print(reduce(multiplication, result_list))  # получается ОГРОМНОЕ число, котроое не поддается .float, так задуманно?

