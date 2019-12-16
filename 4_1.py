file = open('Equation1.txt')
    
expressions = file.readlines()

for expression in expressions:

    brackets = '' 
    for c in expression:
        if c in ('(', ')'):
            brackets = brackets + c
            if c == ')':
                if len(brackets) >= 2: 
                    if brackets[-1] == ')' and brackets[-2] == '(':
                        brackets = brackets[:-2]
    if brackets:
        print('Тут хибно ', expression)
    else:
        print('Тут істинно', expression)
