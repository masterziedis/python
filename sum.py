def sum_all_nums(*args):
    total = 0
    for i in args:
        total += i
    print(total)

nums = (1,2,3,4,5,6)
sum_all_nums(*nums)
