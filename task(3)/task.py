def bin_search(in_val, s_val):     
    left = 0
    right = len(in_val)
    if s_val < in_val[left]:
        return 0
    elif s_val > in_val[right - 1]:
        return len(in_val)

    while left < right:
        cur_pos = (left + right) // 2
        if in_val[cur_pos] >= s_val:
            right = cur_pos
        else:
            left = cur_pos + 1

    return left

    
def get_collectioners(count_of_stickers, diego_stickers, count_of_collectioners, collectioners_stickers):
    diego_stickers = sorted(list(diego_stickers))
    ans = []
    for collectioner_st in collectioners_stickers:
        test = bin_search(diego_stickers, collectioner_st)
        ans.append(str(test))
        
    return "\n".join(ans)


if __name__ == '__main__':
    count_of_stickers = int(input())
    diego_stickers = set(map(int, input().split()))
    count_of_collectioners = int(input())
    collectioners_stickers = list(map(int, input().split()))
    print(get_collectioners(count_of_stickers, diego_stickers, count_of_collectioners, collectioners_stickers))