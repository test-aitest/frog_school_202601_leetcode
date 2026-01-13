'''
https://leetcode.com/problems/valid-anagram/
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # とりあえず解いてみる
        # 1.文字数の一致確認
        # 2.ソートして一致確認
        # First,check if the lengths are different.
        # 2.Then I sort both strings and compare them.
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)