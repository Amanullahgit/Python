def MAD():
    n = input('Enter numbers space seperated: ')
    m = [float(i) for i in n.split()]
    res = 0
    mean = sum(m) / len(m)
    for num in m:
        res = round(res, 2) + abs(num - round(mean, 2))
    mad = round(res / len(m), 2)

    print(f'MAD: {mad}')


while True:
    MAD()
