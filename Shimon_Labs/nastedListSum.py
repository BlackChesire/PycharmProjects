# program to sum all elements in nasted list

def nastedListSum(lst):
    if len(lst) == 0:
        return 0
    if type(lst[0]) == list:
        return nastedListSum(lst[0]) + nastedListSum(lst[1:])
    else:
        return lst[0] + nastedListSum(lst[1:])


print( nastedListSum([1, 2, [3,4],[5,6]]))