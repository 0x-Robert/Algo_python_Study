
from collections import Counter

def find_max(word):
    counter = Counter(word)
    print("counter: ",counter)
    max_count = -1
    for letter in counter:
        print("letter",letter)
        if counter[letter] > max_count:
            max_count = counter[letter]
            print("max_count",max_count)
            max_letter = letter
            print("max_letter",max_letter)
    return max_letter, max_count


find_max('hello world') # ('l', 3)