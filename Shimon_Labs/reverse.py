# Program to change the word sequence to reverse
def reverse_words(s):
    s = s.split()
    s.reverse()
    return ' '.join(s)


print(reverse_words(input("Please enter a sentence: ")))


"""  RUN DEMO
one two three four
four three two one
"""