# Program to ring cyclic shift of a list

# option 1
def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
          
# option 2
def shift2(lst, steps):
    lst[:] = lst[-steps:]+lst[:-steps]


nums = input("Please enter a list of numbers: ").split()
for i in range(len(nums)):
    nums[i] = int(nums[i])
print(nums)

shift2(nums, -2)
print(nums)

shift2(nums, 3)
print(nums)

"""   RUN DEMO
[4, 5, 6, 7, 8, 9, 0]
[6, 7, 8, 9, 0, 4, 5]
[0, 4, 5, 6, 7, 8, 9]
"""
