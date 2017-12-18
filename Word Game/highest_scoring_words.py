'''
- Prompts the user to input between 3 and 10 lowercase letters (with possibly whitespace inserted any-
where); if the input contains too few or too many lowercase letters or any character which is neither a
lowercase letter nor whitespace, then the program outputs an error message and exits.
- Finds in the file wordsEn.txt, assumed to be stored in the working directory, the words built from the
letters input by the user (with the exclusion of any other character) with highest score, if any; the score
of a word is dened as the sum of the values of the letters that make up that word, the value of each
letter being dened as follows:
a 2    b 5    c 4    d 4    e 1    f 6
g 5    h 5    i 1    j 7    k 6    l 3
m 5    n 2    o 3    p 5    q 7    r 2
s 1    t 2    u 4    v 6    w 6    x 7
y 5    z 7

- Outputs a specifc message if there is no such word; otherwise, outputs the highest score and all words
with that score, one word per line, with a dierent introductory message depending on whether there
is a unique such word (in which case the introductory message is on the same line as the word) or at
least two such words (in which case the introductory message is on a line of its own and all words are
preceded with 4 spaces).

Written by Benny Hwang 16/08/2017
'''

import sys

# Create words scoring dictionary
scoring = {'a':2, 'b':5, 'c':4, 'd':4, 'e':1, 'f':6, 'g':5, 'h':5, 'i':1, 'j':7, 'k':6, 'l':3, 'm':5, 'n':2, 'o':3, 'p':5, 'q':7, 'r':2, 's':1, 't':2, 'u':4, 'v':6, 'w':6, 'x':7, 'y':5, 'z':7}
        
user_input = input('Enter between 3 and 10 lowercase letters: ')
input_elements = list(user_input)
sorted_input = []
try:
    for elements in input_elements:
        if elements != ' ':
            if elements.islower():
                sorted_input.append(elements)
            else:
                raise ValueError
    if len(sorted_input) < 3 or len(sorted_input) > 10:
        raise ValueError
           
except ValueError:
    print('Incorrect input, giving up...')
    sys.exit() 

text_file = open('wordsEn.txt','r')
lines = text_file.read().split("\n")
lines_set = set(lines)
found = []

for word in lines_set:
    letters = list(word)
    if len(letters) <= 10:
        valid = True
        for char in letters:
            if char not in sorted_input:
                valid = False
        if valid == True:
            found.append(word)
        #print('in')
        
found_copy = found.copy()
for i in found:
    unsorted = list(i)
    for j in unsorted:
        n = unsorted.count(j)
        m = sorted_input.count(j)
        if n > m:
            found_copy.remove(i)
            break

score_total = []
for i in found_copy:
    score = 0
    char = list(i)
    for element in char:
        ele_score = scoring[element]
        score = score + ele_score
    
    if score > 0:
        score_total.append(tuple([score, i])) 

if len(score_total) > 0:
    score_order = sorted(score_total, reverse = True)  
    highest_word = []
    h = score_order[0]
    highest_score = h[0]
    for i in score_order:
        if i[0] == highest_score:
            highest = i[1]
            highest_word.append(highest)
        else:
            break
    
    print("The highest score is " + str(highest_score) +'.') 
    highest_word = sorted(highest_word)
    if len(highest_word) > 1:
        print("The highest scoring words are, in alphabetical order:")
        for word in highest_word:
            print('    ' + word)
    else:
        print('The highest scoring word is ' + str(highest_word[0]))
else:
    print('No word is built from some of those letters.')
    

