def get_best_string(length):
    first_sym = int(input())
    ans = 0
    for i in range(1, length):
        sym = int(input())
        ans += min(sym, first_sym)
        first_sym = sym
    return ans

if __name__ == '__main__':
    length = int(input())
    print(get_best_string(length))