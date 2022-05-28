# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = word.lower()
    anagram = anagram.lower()
    word = word.replace(' ','')
    anagram = anagram.replace(' ','')
    if (sorted(word) == sorted(anagram)):
        return True
    return False

print(find_anagram('corona virus','carnivorous' ))
