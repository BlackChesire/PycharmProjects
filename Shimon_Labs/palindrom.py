# Program to check if a string is a palindrom
def isPalindrome(s):
	#Termination condition: if one character or less are left
	if (len(s) < 2):
		return 1
	#If first character is not a letter, move to the next character
	if not s[0].isalpha():
		return isPalindrome(s[1:])
	#If last character is not a letter, ignore it by reducing len
	if not s[-1].isalpha():
		return isPalindrome(s[:-1])

	#The first and last character are both letters by now
    #If the first and last letters identical, drop both
	if s[0].lower()==s[-1].lower():
		return isPalindrome(s[1:-1])
	
	#the first and last letter are different. This is not a palindrome
	return 0


#  checking program
if __name__ == '__main__': 
    s = "Was it Eliot's toilet I saw?";
    print("%s is%s a palindrome"%(s, "" if isPalindrome(s) else " not"))
	


