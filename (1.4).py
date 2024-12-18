def convertvdesatich(numbers, base):
    return [int(num, base) for num in numbers]

def convertizdesatich(number, base):
    if number == 0:
        return '0'
    digits = []
    while number:
        digits.append(int(number % base))
        number //= base
    return ''.join(str(x) for x in digits[::-1])

with open('input.txt', 'r') as file:
    lines = file.readlines()

numbers = lines[0].strip().split()
operation = lines[1].strip()
base = int(lines[2].strip())

desatich = convertvdesatich(numbers, base)

if operation == '+':
    result = sum(desatich)
elif operation == '-':
    result = desatich[0] - sum(desatich[1:])
elif operation == '*':
    result = 1
    for number in desatich:
        result *= number
else:
    result = "Ошибка: неизвестная операция"

result_in_base = convertizdesatich(result, base)

with open('output.txt', 'w') as file:
    file.write(result_in_base)