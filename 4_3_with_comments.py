from sympy import *
from sympy.solvers.solveset import linsolve


def normalize_equation(eq):
    s = ''

    for c in range(len(eq) - 1): # Проходимо вираз посимвольно і знавим на місці доміка ^ - **, і знак множення якшо він не стоїть.

        if eq[c] == '^':
            s += '**'
            continue

        s += eq[c]

        if eq[c + 1] == 'x' and eq[c] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            s += '*'

    s += eq[-1]

    return s


file = open('lab11.txt') # Відкриваємо файл

expressions = file.readlines() # Зчитуємо всі рядки із файлу

file.close() # Файл закриваємо. Адже ми все зчитали і він більше не треба


for expression in expressions: # перебираємо всі вирази. У expression буде спочатку -x^2+5x-4=0 потім x^4+3x^2-7<=0 і так далі. Див lab11.txt

    expression = expression.strip() # Обрізаємо пробіли по краях якщо вони є
    print('-----------------------------------------')

    # Визначаємо чи це рівняння чи нерівність
    if '<' in expression or '>' in expression: # Якшо вираз містить символи < або > то виводимо що це рівняння або нерівність. 
        rivnanya = 0 # Якшо це нерівність, то у змінну rivnanya записуємо 0
        print(expression, '-', 'нерівність')
    else:
        rivnanya = 1 # Якшо це рівняння, то у змінну rivnanya записуємо 1. Потім пригодиться.
        print(expression, '-', 'рівняння')

    # Знаходимо найбільшу степінь
    if '^' in expression: # Якшо у виразі є символ ^ це означає шо у нас є степінь. 
        max_power = 0 # Створюємо змінну і записуємо спочатку нуль
        for c in range(len(expression) - 1): # Перебираємо всі символи у виразі і якщо знаходим степінь більшу за 0 то записуємо її значення у max_power
            if expression[c] == '^':
                if int(expression[c + 1]) > max_power: # І так кожного разу. Якщо знаходим степінь більшу аніж уже була записана, то записуємо її.
                    max_power = int(expression[c + 1])

        print('Максимальна степінь:', max_power) # І виводимо

    expression = normalize_equation(expression) # Ця функція заміняє символи щоб вираз став валідним для обчислення. ^ замінуємо на ** (бо степінь у пітоні це дві зірочки - **). Якщо немає знаку множення то його теж додаєм. Оскільки 3х - це невалідний формат, а 3*х - цей заєбісь.

    if rivnanya: # Значить згадуй про змінну rivnanya. Якшо вона = одиниці то це рівнння, інакше це нерівність.  Ця штука треба, бо для того щоб нам далі отримати коефіцієнти то треба взяти частину виразу до дорівнює(якшо це рівння) або до знаків більше,менше. Тобто із 4*x=12 отримуємо 4*х, і із 4*x > 0 отримуємо 4*x
        expression = expression.split('=')[0]
    else:
        if '<' in expression:
            expression = expression.split('<')[0]
        elif '>':
            expression = expression.split('>')[0]
            
    x = symbols('x') # Код треба для того щоб отримати коефіцієнти. Можеш глянути тут https://vike.io/ru/289663/
    a = Poly(expression, x)
    print('Коефіцієнти:', a.coeffs())
    
    answer = solve(expression, x) # Собствєнно функція solve вирішує рівняння чи нерівність і у змінну answer заносить результат.

    if str(answer) in ['True', 'False']: # Тут зрозуміло. Якшо answer - тру або фолс, то пишемо мол вся множина розв, або їх немає або ж виводим конкретний розвязок.
        if answer:
            print('Відповідь:', 'вся множина розв\'язків')
        else:
            print('Відповідь:', 'немає розв\'язків')
    else:
        print('Відповідь:', answer)