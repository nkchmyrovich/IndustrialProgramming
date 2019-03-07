input_list = []
input_list = list(input().split(', '))
positive_list = []
for it in input_list:
    if it[0] == '-':
        positive_list.append(it[1:])
    else:
        positive_list.append(it)



def get_sum_figs(num):
    string = str(num)
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
    string = str(num)
    a = num
    while int(a) >= 10:
        a = get_sum_figs(a)
    if a == '3' or a == '6' or a == '9':
        return True
    else:
        return False

result = []
for i in range(len(positive_list)):
    string = ""
    change = False
    if is_divisible_by_three(positive_list[i]):
        string += "fizz"
        change = True
    if is_divisible_by_five(positive_list[i]):
        string += "buzz"
        change = True
    if change:
        result.append(string)
    else:
        result.append(input_list[i])

print(result)

