file = open('lab1.txt')

expressions = file.readlines()

for expression in expressions:

    mathematical_operations = ['+', '-', '*', '/']
    operations_count = 0

    for operation in mathematical_operations:
        operations_count = operations_count + expression.count(operation)

    print('Вираз:', expression, end='')
    print('Кількість операцій:', operations_count)
    print('Результат обчислення:', eval(expression))
    print()
