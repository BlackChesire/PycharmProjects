# Program to build a list of the length of elements in lansted list without a given word

def wordLenList(s,w):
    words = s.split()
    wordLengths = [len(word) for word in words if word != w]
    return wordLengths

#checking program
sentence = "the quick brown fox jumps over the lazy dog"
print(wordLenList(sentence,'the'))
