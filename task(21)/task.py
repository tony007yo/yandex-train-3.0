def calculate(num):
    l = [2, 4, 7]
    for i in range(3, num):
        l.append(l[i-1] + l[i-2] + l[i-3])
    return l[num - 1]

if __name__ == '__main__':
    print(calculate(int(input())))