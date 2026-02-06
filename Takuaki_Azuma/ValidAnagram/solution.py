class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # check the length
        if len(s) != len(t):
            return False

        #2 Initialize manual counter(dictionary)
        count = {}

        #3 count charactors in string 's'
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        #4 subtract counts using string 't'
        for char in t:
            if char not in count:
                return False
            
            count[char] -= 1

            if count[char] < 0:
                return False
        
        #If we pass all checks, it is an anagram
        return True