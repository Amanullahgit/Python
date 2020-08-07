def percentile():
    n = input('Enter numbers space seperated: ')
    p = input('Enter Percentile: ')

    m = [int(i) for i in n.split()]
    m.sort()
    print(m)
    print((float(p)/100)*len(m))
    ans = (float(p)/100)*len(m)

    if ans.is_integer():
        print(m[int(float(ans-1))])
        print(m[int(float(ans))])
        print((m[int(float(ans-1))] + m[int(float(ans))])/2)
    else:
        print(m[round(float(ans))])


while True:
    percentile()