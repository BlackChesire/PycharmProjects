# Accessing an item by a nonexistent index
a = [1.2, 1.8, 3.2, 2.5, 1.7, 2.6, 0.5]

print("s - stop")

while True:
    indx = input("ID: ")
    if indx == 's':
        break
    try:
        indx = int(indx)
        print(a[indx])
    except ValueError:
        print("Must be an integer!")
    except IndexError:
        print("No item with ID =", indx)