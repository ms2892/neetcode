import collections


class Solution:
    def isAnagram(self,s,t):
        # Function
        # This function checks whether the two given strings are anagrams or not
        # Inputs:
        #   s   (string)    Contains string1
        #   t   (string)    Contains string2
        # Outputs:
        #   (bool)      returns True is string1 and string2 are anagrams; False otherwise
        
        # If both strings have equal and same number of characters, then the strings are an Anagram
        
        # collections.Counter(s) counts the frequency of each letter in an iterable object
        # (e.g: {'a':2,'b':5})
        
        # If both the strings have the same distribution of letters then they are Anagrams else they are not
        return collections.Counter(s) == collections.Counter(t)