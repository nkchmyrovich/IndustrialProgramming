def process_input_data(input):
    positive_data = []
    for it in input:
        if it[0] == '-':
            positive_data.append(it[1:])
        else:
            positive_data.append(it)
    result = []
    for i in range(len(positive_data)):
        string = ""
        change = False
        if is_divisible_by_three(positive_data[i]):
            string += "fizz"
            change = True
        if is_divisible_by_five(positive_data[i]):
            string += "buzz"
            change = True
        if change:
            result.append(string)
        else:
            result.append(input[i])
    return result


def string_positive(string):
    if string[0] == '-':
        return string[1:]
    else:
        return string


def get_sum_figs(num):
    string = string_positive(str(num))
    _sum = 0
    for char in string:
        _sum += int(char)
    return str(_sum)


def is_divisible_by_five(num):
    string = str(num)
    last_fig = int(string[-1])
    if last_fig == 5 or last_fig == 0:
        return True
    else:
        return False


def is_divisible_by_three(num):
    a = num
    while int(a) >= 10:
        a = get_sum_figs(a)
    if a == '3' or a == '6' or a == '9':
        return True
    else:
        return False


def main():
    input = list(input().split(', '))
    output = process_input_data(input)
    print(output)