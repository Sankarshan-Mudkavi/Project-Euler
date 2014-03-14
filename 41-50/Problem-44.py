def p_number(n):
    return (n * ((3 * n) - 1)) / 2

def gen_a_lot_of_p():
    min_list = []
    p_dict = {}
    for i in range(1, 16000):
        p_dict[p_number(i)] = i
    for num in p_dict:
        for num_1 in p_dict:
            if num != num_1:
                if num_1 + num in p_dict:
                    if abs(num_1 - num) in p_dict:
                        print num_1, num
                        min_list.append(abs(num_1 - num))
    return min(min_list)


print gen_a_lot_of_p()