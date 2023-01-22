def five_num():
    n = input('Enter numbers space seperated: ')
    m = [float(i) for i in n.split()]
    m.sort()
    med = (len(m) + 1) / 2
    q1 = (25 / 100) * len(m)
    q3 = (75 / 100) * len(m)
    q1_res = (m[int(q1 - 1)] + m[int(q1)]) / 2
    q3_res = (m[int(q3 - 1)] + m[int(q3)]) / 2
    largest_num = m[len(m) - 1]
    smallest_num = m[0]
    print(f'Smallest Value: {round(smallest_num,3)}')
    print(f'Q1: {round(q1_res,3)}')
    if med.is_integer():
        print(f'Median (M): {m[int(med - 1)]}')
    else:
        print(f'Median (M): {(m[int(med - 1)] + m[int(med)]) / 2}')
    print(f'Q3: {round(q3_res,3)}')
    print(f'Largest Value: {round(largest_num,3)}')


while True:
    five_num()
