class B:
    __count = 0
    x=0

    def __init__(self):
        self.__one=1
        B.__count += 1

    def __del__(self):
        B.__count -= 1

    def qty_objects():
        two=0
        return B.__count


a = B()
b = B()
c = B()
print(b.qty_objects())
del a
print(B.qty_objects())
print(b.qty_objects())
