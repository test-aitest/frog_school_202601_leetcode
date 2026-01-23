"""
Koko Eating Bananas
Medium

You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.

Constraints:

1 <= piles.length <= 1,000
piles.length <= h <= 1,000,000
1 <= piles[i] <= 1,000,000,000

https://neetcode.io/problems/eating-bananas/question?list=neetcode150
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        k is the number of bananas you can eat during 1 hour. This is speed of eating bananas.
        you have to return minimum k.
        Maybe you can use binary search algorighm. You look minimum k. l ~ k ~ r.
        """