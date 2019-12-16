file = open('lab1.txt') # Відкриваємо файл

expressions = file.readlines() # Читаєм все

for expression in expressions: # Перебираємо прочитані із файлу вирази

    mathematical_operations = ['+', '-', '*', '/'] # Список математичних операцій які ми будемо рахувати
    operations_count = 0 # лічильник де буде записана загальна кількість операцій

    for operation in mathematical_operations: # Якшо ми знаходимо те що нас цікавить - збільшуєм лічильник на 1
        operations_count = operations_count + expression.count(operation)

    print('Вираз:', expression, end='') # Виводим собтвєнно вираз
    print('Кількість операцій:', operations_count) # змінну де записано кількість операцій
    print('Результат обчислення:', eval(expression)) # І результат. Функція eval() обрахуовує вирази. Приклади тут -  https://thepythonguru.com/python-builtin-functions/eval/
    print()
