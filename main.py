# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(first_word, second_word):
    # [assignment] Add your code here
    sortword1 = sorted(first_word)
    sortword2 = sorted(second_word)
    if sortword1 == sortword2:
        print("True")
        return True
    else:
        print("False")
        return False

find_anagram("below", "elbow")

