# program to convert an integer to a string in any base

def intToStringBase(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return intToStringBase(n//base,base) + convertString[n % base]

def main():
    num = int(input("please enter a number: "))
    print("%d in binary base: %s"%(num,intToStringBase(num,2)))
    print("%d in octal base: %s"%(num,intToStringBase(num,8)))
    print("%d in hexadecimal base: %s"%(num,intToStringBase(num,16)))
    
main()