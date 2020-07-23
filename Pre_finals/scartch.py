def bubblesort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def binary_search(lst, value):
    high = len(lst)
    low = 0
    while high > low:
        mid = (low + high) // 2
        if lst[mid] == value:
            return mid
        elif lst[mid] < value:
            low = mid + 1
        else:
            high = mid


def is_palindrome(string):
    string = [i for i in string if i.isalpha()]
    if string[0] != string[-1]:
        return False
    if len(string) == 1:
        return True
    elif string[0] == string[-1]:
        return is_palindrome(string[1:-1])


def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def multiply_lst(lst1, lst2):
    lst3 = [lst1[i] * lst2[i] for i in range(len(lst1))]
    return lst3


def lst_splitter(lst, num):
    lst_splitted = [[lst[j] for j in range(j, j + 2)] for j in range(0, num)]
    return lst_splitted


def nested_maker(n):
    nested = [[i for i in range(1, j)] for j in range(2, n + 1)]
    return nested


def flatten_matrix(mat):
    flatted_mat = [mat[i][j] for i in range(len(mat)) for j in range(len(mat[i]))]
    return flatted_mat


def max_list(lst1, lst2):
    lst3 = [lst1[i] if lst1[i] > lst2[i] else lst2[i] for i in range(len(lst1))]
    return lst3


def bin_search(lst, i):  # recursive binary search
    mid = len(lst) // 2
    if not mid:
        return
    if (v := lst[mid]) != i:
        res = bin_search(lst[mid:], i)
        if v < i:
            return res + mid if res else 0
        else:
            return res - mid if res else 0
    else:
        return mid


def multiply_scalar(n, arr):
    multiplied_list = [[x * n for x in y] for y in arr]
    return multiplied_list


def add_mat(arr1, arr2):
    added_mat = [[arr1[i] + arr2[i]] for i in range(len(arr1))]
    return added_mat


def is_magic_square(mat):
    rows = [sum(mat[j]) for j in range(len(mat))]
    cols = [sum([mat[i][j] for i in range(len(mat))]) for j in range(len(mat))]
    cross = [sum(mat[c][c] for c in range(len(mat)))]
    # cross2 == pass
    return cross[0] == cols[0] == rows[0]


def spiderman(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return spiderman(n - 1) + spiderman(n - 2)


def func(n, k):  # print(func(1, 3)) = 4
    if n == 0 or k == 0:
        return 1
    return func(n - 1, k) + func(n, k - 1)


def get_one_number(numbers):
    # if no numbers -> problem
    if len(numbers) == 0:
        return None
    # if only 1 element return it
    if len(numbers) == 1:
        return numbers[0]
    # if more than one element:
    #   get one number from the list starting at position 1
    next = get_one_number(numbers[1:])
    #   find out the length of this number by counting divisions by 10
    next_copy = next
    length = 0
    while next_copy > 0:
        next_copy //= 10
        length += 1

    # multiply the first number by the length of the rest's "one number" and add that one number
    return numbers[0] * (10 ** length) + next


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def DictOfdiv(lst):
    d = {}
    for i in lst:
        d[i] = [j for j in range(1,i) if i%j == 0]
    return d


print(DictOfdiv([36,15,6]))