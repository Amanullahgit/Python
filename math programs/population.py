import math


def population_variance():
    n = input('Enter numbers space seperated: ')
    m = [float(i) for i in n.split()]
    res = 0
    print(m)
    mean = sum(m) / len(m)
    print(mean)
    for num in m:
        res = round(res, 2) + pow(num - round(mean, 2), 2)
    population_var = round(res / len(m), 2)
    sample_var = round(res / (len(m) - 1), 2)
    population_standard_deviation = math.sqrt(population_var)
    sample_standard_deviation = math.sqrt(sample_var)
    print(f'population variance: {population_var}')
    print(f'sample variance: {sample_var}')
    print(f'population standard deviation: {round(population_standard_deviation, 2)}')
    print(f'sample standard deviation: {round(sample_standard_deviation, 2)}')


while True:
    population_variance()
