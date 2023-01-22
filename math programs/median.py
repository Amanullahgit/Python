
def median():
    n = input('Enter numbers space seperated: ')
    m = [int(i) for i in n.split()]

    m.sort()
    med = (len(m) + 1) / 2
    if med.is_integer():
        print(f'Median (M): {m[int(med - 1)]}')
    else:
        print(f'Median (M): {(m[int(med - 1)] + m[int(med)]) / 2}')


while True:
    median()



