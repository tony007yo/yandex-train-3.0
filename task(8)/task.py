def main():
    def calc_min_max(seq):
        seq = list(seq)
        min_n = seq[0]
        max_n = seq[0]
        for i in range(1, len(seq)):
            if seq[i] < min_n:
                min_n = seq[i]
            elif seq[i] > max_n:
                max_n = seq[i]
        
        return (min_n, max_n)

    size = int(input())
    set_x = set()
    set_y = set()
    for i in range(size):
        x, y = map(int, input().split())
        set_x.add(x)
        set_y.add(y)
    x0, x1 = calc_min_max(set_x) 
    y0, y1 = calc_min_max(set_y)
    print(x0, y0, x1, y1)
    
if __name__ == '__main__':
    main()