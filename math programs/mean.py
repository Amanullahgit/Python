def mean():
    n = input('Enter numbers space seperated: ')
    m = [int(i) for i in n.split()]
    print(f'Mean (x-bar): {sum(m) / len(m)}')


while True:
    mean()
