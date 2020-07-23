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


"""lst = [5, 4, 3]
subSetSums(lst)
"""