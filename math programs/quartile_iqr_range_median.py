def quartile():
    n = input('Enter numbers space seperated: ')
    m = [float(i) for i in n.split()]
    m.sort()
    med = (len(m) + 1) / 2
    q1 = (25 / 100) * len(m)
    q2 = (50 / 100) * len(m)
    q3 = (75 / 100) * len(m)
    q1_res = (m[int(q1 - 1)] + m[int(q1)]) / 2
    q2_res = (m[int(q2 - 1)] + m[int(q2)]) / 2
    q3_res = (m[int(q3 - 1)] + m[int(q3)]) / 2
    largest_num = m[len(m) - 1]
    smallest_num = m[0]
    iqr = round(q3_res,3) - round(q1_res,3)
    rang = m[len(m) - 1] - m[0]
    print(f'Smallest Value: {round(smallest_num,3)}')
    print(f'Largest Value: {round(largest_num,3)}')
    print(f'Q1: {round(q1_res,3)}')
    print(f'Q2: {round(q2_res,3)}')
    print(f'Q3: {round(q3_res,3)}')
    print(f'IQR: {round(iqr,3)}')
    print(f'Range: {round(rang,3)}')
    if med.is_integer():
        print(f'Median (M): {m[int(med - 1)]}')
    else:
        print(f'Median (M): {(m[int(med - 1)] + m[int(med)]) / 2}')

while True:
    quartile()
