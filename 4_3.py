from sympy import *
from sympy.solvers.solveset import linsolve


def normalize_equation(eq):
    s = ''

    for c in range(len(eq) - 1):

        if eq[c] == '^':
            s += '**'
            continue

        s += eq[c]

        if eq[c + 1] == 'x' and eq[c] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            s += '*'

    s += eq[-1]

    return s


file = open('lab11.txt')

expressions = file.readlines()

file.close()


for expression in expressions:

    expression = expression.strip()
    print('-----------------------------------------')

    if '<' in expression or '>' in expression:
        rivnanya = 0
        print(expression, '-', 'нерівність')
    else:
        rivnanya = 1
        print(expression, '-', 'рівняння')

    if '^' in expression:
        max_power = 0
        for c in range(len(expression) - 1):
            if expression[c] == '^':
                if int(expression[c + 1]) > max_power:
                    max_power = int(expression[c + 1])

        print('Максимальна степінь:', max_power)

    expression = normalize_equation(expression)

    if rivnanya:
        expression = expression.split('=')[0]
    else:
        if '<' in expression:
            expression = expression.split('<')[0]
        elif '>':
            expression = expression.split('>')[0]
            
    x = symbols('x')    
    a = Poly(expression, x)
    print('Коефіцієнти:', a.coeffs())
    
    answer = solve(expression, x)

    if str(answer) in ['True', 'False']:
        if answer:
            print('Відповідь:', 'вся множина розв\'язків')
        else:
            print('Відповідь:', 'немає розв\'язків')
    else:
        print('Відповідь:', answer)
