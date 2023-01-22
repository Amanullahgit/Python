from collections import Counter


def median(lst):
    lst.sort()
    med = (len(lst) + 1) / 2
    if med.is_integer():
        print(f'Median (M): {lst[int(med - 1)]}')
        return lst[int(med - 1)]
    else:
        print(f'Median (M): {(lst[int(med - 1)] + lst[int(med)]) / 2}')
        return (lst[int(med - 1)] + lst[int(med)]) / 2


def mean(lst):
    print(f'Mean (x-bar): {round(sum(lst) / len(lst),4)}')
    return round(sum(lst) / len(lst),4)


def mode():
    n = input('Enter numbers space seperated: ')
    m = [float(i) for i in n.split()]

    a = dict(Counter(m))
    key_list = list(a.keys())
    val_list = list(a.values())

    if max(val_list) > 1:
        print(f'Mode (Z): {key_list[val_list.index(max(val_list))]}')
    else:
        men = mean(m)
        med = median(m)
        print(f'Mode (Z): {round((3 * med) - (2 * men),4)}')


while True:
    mode()
