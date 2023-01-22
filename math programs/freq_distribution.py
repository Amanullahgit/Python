def freq_cw():
    n = input('Enter numbers space seperated: ')
    cw = int(input('Enter class width: '))
    m = [float(i) for i in n.split()]
    m.sort()
    counter = 0
    cumulative_freq = 0
    frequencies = []
    mid_point = []
    lower_bound = int(m[0])
    upper_bound = lower_bound + cw
    number_of_times = int((int(m[0]) + int(m[len(m) - 1])) / cw)
    while number_of_times > 0:
        for num in m:
            if num in range(lower_bound, upper_bound):
                counter += 1

        print(f'{lower_bound} - {upper_bound}: {counter}')
        mid_point.append((lower_bound + upper_bound) / 2)
        frequencies.append(counter)
        lower_bound = upper_bound
        upper_bound = lower_bound + cw
        counter = 0
        number_of_times -= 1

    for i in range(len(frequencies)):
        relative_freq = int((frequencies[i] / sum(frequencies)) * 100) / 100
        percent_freq = int(relative_freq * 100)
        cumulative_freq = cumulative_freq + frequencies[i]
        print(
            f'Freq {frequencies[i]}: Mid => {mid_point[i]}, Relative: {relative_freq}, Percentage: {percent_freq}%, Cumulative Freq: {cumulative_freq}')


def freq_no_cw():
    n = input('Enter numbers space seperated: ')
    cint = int(input('Enter class interval: '))
    m = [float(i) for i in n.split()]
    m.sort()
    cw = int(((m[len(m)-1] - m[0]) / cint) + 1)
    counter = 0
    cumulative_freq = 0
    frequencies = []
    mid_point = []
    lower_bound = int(m[0])
    upper_bound = lower_bound + cw
    number_of_times = int((int(m[0]) + int(m[len(m) - 1])) / cw)
    print(number_of_times)
    while number_of_times > 0:
        for num in m:
            if num in range(lower_bound, upper_bound):
                counter += 1

        print(f'{lower_bound} - {upper_bound}: {counter}')
        mid_point.append((lower_bound + upper_bound) / 2)
        frequencies.append(counter)
        lower_bound = upper_bound
        upper_bound = lower_bound + cw
        counter = 0
        number_of_times -= 1

    for i in range(len(frequencies)):
        relative_freq = int((frequencies[i] / sum(frequencies)) * 100) / 100
        percent_freq = int(relative_freq * 100)
        cumulative_freq = cumulative_freq + frequencies[i]
        print(
            f'Freq {frequencies[i]}: Mid => {mid_point[i]}, Relative: {relative_freq}, Percentage: {percent_freq}%, Cumulative Freq: {cumulative_freq}')


while True:
    ask = input('have class width? ')
    if ask == 'y':
        freq_cw()
    else:
        freq_no_cw()
