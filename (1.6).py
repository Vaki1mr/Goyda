def reverse_groups(g, input_string):
    n = len(input_string)
    group_length = n // g
    reversed_groups = []

    for i in range(0, n, group_length):
        group = input_string[i:i + group_length]
        reversed_groups.append(group[::-1])

    result = ''.join(reversed_groups)
    return result


g = int(input("Введите количество групп: "))
input_string = input("Введите строку: ")
output_string = reverse_groups(g, input_string)
print(output_string)