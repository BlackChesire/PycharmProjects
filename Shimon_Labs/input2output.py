# Program to print to an output file all the 2nd words from an input file 

inp=open('input.txt','r')
content = inp.read()
inp.close()
words=content.split()
even_words=words[::2]
even_words_string = ' '.join(even_words)
out=open('output.txt','w')
out.write(even_words_string)
out.close()


    