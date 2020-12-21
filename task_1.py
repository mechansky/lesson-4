from sys import argv

script_name, production, rate, bonus = argv


def payment(production, rate, bonus):
      result = (int(production) * int(rate)) + int(bonus)
      return result


print(f'Выработка в часах: {production}\n'
      f'Ставка в час: {rate}\n'
      f'Премия: {bonus}\n')
print(f'заработная плата сотрудника составляет {float(payment(production, rate, bonus))} руб.')


