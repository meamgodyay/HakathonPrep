from __future__ import print_function
from PyDictionary import PyDictionary
from nltk.corpus import words

dictionary = PyDictionary()

final_answer = []
list_module = []

word = str(input("Please enter the word you would like to check for anagrams\n")).lower()
word_module = list(word)

all_words = words.words()

number_letter_words = [word for word in all_words if len(word) == len(word_module)]


for word in number_letter_words: 
    list_module.append(word)
    
# for i in list_module:
#     module = list(i)
#     common = [item for item in module if item in word_module]
#     if len(common) == len(word_module):
#         final_answer.append(i)

epoxy = 0

for i in list_module:
    module = list(i)
    for a in word_module:
        if a in module:
            epoxy = epoxy + 1
        elif a not in module:
            epoxy = epoxy
    if epoxy == len(word_module):
        final_answer.append(i)
    
    epoxy = 0    
    
if len(final_answer) == 0:
    print("This word has no valid anograms that are actual words. Check the spelling")
    word = str(input("Please enter the word you would like to check for anagrams\n")).lower()
else:
    print(f"Your word has {len(final_answer)} valid anagrams: \n" + '\n'.join(final_answer))    


    

