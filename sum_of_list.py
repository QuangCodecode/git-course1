def sum_list(alist):
    total = 0
    for i in alist:
        if type(alist) != int:
            continue
        total += i
    return total