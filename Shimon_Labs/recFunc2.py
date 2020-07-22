def me_ani(n):
    if n<10:
        return n
    else:
        i=10
        while n%i!=n:
            i*=10
        return ((n%10)*i//10)+me_ani(n//10)
def main():
    n=23456
    print(me_ani(n))

main()
        

        
    