# coding: utf-8
# %load http://tinyurl.com/count-words-ex
"""
Write a program to count the number of occurrence of each word in a string
delimited by white-spaces.

Example usage:
--------------
   >>> quote = '''
   ... When I see a bird
   ... that walks like a duck
   ... and swims like a duck
   ... and quacks like a duck,
   ... I call that bird a duck
   ... '''

   >>> count_words(quote)
   'When' occurs 1 times
   'I' occurs 2 times
   'see' occurs 1 times
   'a' occurs 5 times
   'bird' occurs 2 times
   'that' occurs 2 times
   'walks' occurs 1 times
   'like' occurs 3 times
   'duck' occurs 3 times
   'and' occurs 2 times
   'swims' occurs 1 times
   'quacks' occurs 1 times
   'duck,' occurs 1 times
   'call' occurs 1 times

   >>>

"""
def count_words(line):
    count = {}
    for w in line.split():
        if w not in count:
            count[w] = 0
        # or we can count[w] = count.get(w,0) +1
        count[w] += 1
    for w, c in count.items():
        print(f"{w} occured in {c} times")

count_words("My name is rovindra is name")
#if __name__ == '__main__':
#    import doctest
#    doctest.testmod()
