def calculate_var(pos, num_of_line, count_of_variants):
    res = None
    if pos % 2 == 1:
        res = ((num_of_line - 1) * 2 + 1) % count_of_variants
    else:
        res = ((num_of_line) * 2) % count_of_variants

    if res == 0:
        res = count_of_variants
    
    return res

def find_Vasya_place(count_of_pupil, count_of_variants, num_of_line, pos_of_Petya):
    is_bin = not bool(count_of_variants % 2)
    res_left = None
    res_right = None
    res_last = None

    petya_var = calculate_var(pos_of_Petya, num_of_line, count_of_variants)

    if is_bin:
        max_dist_bin = (count_of_variants // 2)
        res_left = (num_of_line - max_dist_bin, pos_of_Petya)
        res_right = (num_of_line + max_dist_bin, pos_of_Petya)
    else:
        search_pos = 3 - pos_of_Petya
        max_dist_right = (count_of_variants // 2) + 1
        max_dist_left = (count_of_variants // 2)
        calc_left = None
        calc_right = None

        if petya_var == calculate_var(search_pos, num_of_line - max_dist_left, count_of_variants) and \
            petya_var == calculate_var(search_pos, num_of_line + max_dist_right, count_of_variants):
            calc_left = max_dist_left
            calc_right = max_dist_right
        elif petya_var == calculate_var(search_pos, num_of_line - max_dist_right, count_of_variants) and \
            petya_var == calculate_var(search_pos, num_of_line + max_dist_left, count_of_variants):
            calc_left = max_dist_right
            calc_right = max_dist_left
        
        res_left = (num_of_line - calc_left, search_pos)
        res_right = (num_of_line + calc_right, search_pos)

    
    if res_left and res_left[0] <= 0:
        res_left = None

    if res_right and (res_right[0] * 2 - (res_right[1]) % 2) > count_of_pupil:
        res_right = None
    

    if res_left and res_right:
        if res_right[0] - num_of_line <= num_of_line - res_left[0] and (res_right[0] * 2 - (res_right[1]) % 2) <= count_of_pupil:
            res_last = res_right
        else:
            res_last = res_left
    
    return res_last or res_left or res_right

if __name__ == '__main__':
    count_of_pupil = int(input())
    count_of_variants = int(input())
    num_of_line = int(input())
    pos_of_Petya = int(input())
    res = find_Vasya_place(count_of_pupil, count_of_variants, num_of_line, pos_of_Petya)
    if res:
        print(f"{res[0]} {res[1]}")
    else:
        print(-1)
