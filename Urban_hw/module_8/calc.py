def calc(line):
    operand1, operation, operand2 = line.split(' ')
    operand1 = int(operand1)
    operand2 = int(operand2)
    """print(operand1, operation, operand2)
    if operation == '+':
        print(f'{operand1 + operand2}')
    if operation == '-':
        print(f'{operand1 - operand2}')
    if operation == '*':
        print(f'{operand1 * operand2}')
    if operation == '/':
        print(f'{operand1 / operand2}')
    if operation == '//':   # целочисленное деление
        print(f'{operand1 // operand2}')
    if operation == '%':  # остаток от деления
        print(f'{operand1 % operand2}')"""

count = 0

with open('calc.txt', 'r') as file:
    for line in file:
        count += 1
        try:
            calc(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                # print(f"Error in {count} to param {exc.args}")
                print(f"Error in {count} не хватает данных для ответа")
            else:
                print(f"Error in {count} нельзя перевести в число")
