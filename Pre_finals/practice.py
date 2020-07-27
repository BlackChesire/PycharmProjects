def bubbleSortRec(lst):
    if len(lst) <= 1:
        return
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
    bubbleSortRec(lst[:-1])


def bubble_sort(arr):
    lentgh = len(arr)
    for i in range(lentgh):
        for j in range(lentgh - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def subs(l):
    if l == []:
        return [[]]
    x = subs(l[1:])
    return x + [[l[0]] + y for y in x]


def howManyWays(lst, n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    res = 0
    for num in lst:
        res += howManyWays(lst, n - num)
    return res

def SubSetSUM(a, n):
      if n == 0:
            return True
      if len(a) == 0:
            return False
      big = max(a)
      if big<=n:
            n=n-big
      a.remove(big)
      return SubSetSUM(a, n)                



def insertionSortRecursive(lst):
    n = len(lst)
    if n <= 1:
        return
    insertionSortRecursive(lst[:-1])
    last = lst[n - 1]
    j = n - 2
    while (j >= 0 and lst[j] > last):
        lst[j + 1] = lst[j]
        j -= 1

    lst[j + 1] = last


def merge(A, B):
    """ Merge sorted lists A and B """
    m = len(A);
    n = len(B)
    C = [0] * (m + n)
    i = 0;
    j = 0;
    k = 0

    while i < m and j < n:
        if A[i] < B[j]:
            C[k] = A[i]
            i += 1
        else:
            C[k] = B[j]
            j += 1
        k += 1

    C[k:] = A[i:] + B[j:]  # append what's left
    return C


def mergesort(lst):
    """ recursive mergesort """
    n = len(lst)
    if n <= 1:
        return lst
    return merge(mergesort(lst[:n // 2]),
                 mergesort(lst[n // 2:]))


def selection_sort_short(s):
    ''' sorts s using the selection sort algorithm'''
    m = 0
    for i in range(len(s), 0, -1):
        m = s[0:i].index(max(s[0:i]))
        s[m], s[i - 1] = s[i - 1], s[m]


def binary_search(lst, value):
    """ search for value in lst assuming that lst is sorted. """
    low = 0
    high = len(lst)
    while high > low:
        mid = (high + low) // 2
        if lst[mid] == value:
            return mid
        elif lst[mid] < value:
            low = mid + 1
        else:  # lst[mid] > value
            high = mid
    return -1


def factorial(n):
    """ computes 1*2*...*n """
    if n <= 1:
        return 1
    return factorial(n - 1) * n


def rec_fibo(n):
    """ returns the nth fibonacci number
    (numbering starts from 0) """
    if n <= 1:
        return 1
    return rec_fibo(n - 1) + rec_fibo(n - 2)


def is_palindrome(string):
    string = [i for i in string if i.isalpha()]
    if string[0] != string[-1]:
        return False
    if len(string) == 1:
        return True
    elif string[0] == string[-1]:
        return is_palindrome(string[1:-1])


def fibo(n):
    f1 = f2 = 1
    print(f1, f2, end=' ')
    while n > 2:
        buff = f2
        f2 = f1 + f2
        f1 = buff
        print(f2, end=' ')
        n -= 1
    print()


def recsubSetSums(lst, l, r, sum=0):    # sums of all subsets
    # Print current subset
    if l > r:
        print(sum, end=" ")
        return
    recsubSetSums(lst, l + 1, r, sum + lst[l])
    recsubSetSums(lst, l + 1, r, sum)


def subSetSums(lst):
    n = len(lst)
    recsubSetSums(lst, 0, n - 1)

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
        if len(numbers) == 0:
            return None
        if len(numbers) == 1:
            return numbers[0]
        rest = get_one_number(numbers[1:])
        temp = rest
        length = 0
        while temp > 0:
            temp //= 10
            length += 1
        return numbers[0] * (10 ** length) + rest

    print(get_one_number(numbers))

    def factorial(n):
        if n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    def DictOfdiv(lst):
        d = {}
        for i in lst:
            d[i] = [j for j in range(1, i) if i % j == 0]
        return d

    """Output: ({12:[2,3,4,6], 36:[2,3,4,6,9,12,18], 52:[2,3,13,26]})"""

    def printforward(n):  # compress recuresion
        if n == 0:
            return
        printforward(n - 1)
        print(n)

    def i_len(num: int):
        i = 0
        while num:
            i += 1
            num //= 10
        return i

    def pairs2dict(lst):
        d = {}
        for key, value in lst:
            if key not in d.keys():
                d[key] = [value]
            else:
                d[key].append(value)
        return d

    def max_of_all(lst):
        return lambda x: max([f(x) for f in lst])

    def reduce(f, lst):
        first = lst[0]
        for i in lst[1:]:
            first = f(first, i)
        return first

    def func(x, y):
        return x + y

    def maxList(lst):
        def maxList(lst):
            if len(lst) == 1:
                return lst[0]
            bgst = maxList(lst[1:])
            if lst[0] > bgst:
                return lst[0]
            else:
                return bgst

    def find_num(lst, n):
        index = 0
        if lst[0] == n:
            return index
        if len(lst) == 1 and lst[0] != n:
            return -1
        index += 1
        return index + find_num(lst[1:], n)

    def func(lst_func):
        return lambda x: sum([i(x) for i in lst_func]) / len(lst_func)

    a = func([lambda x: x ** 2 + 5 * x + 5, lambda x: x * 2, lambda x: x])
    a(5)




