from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Returns true if any value appears at least twice in the array.
        """
        # We use a set to keep track of seen numbers because set lookups are O(1) on average.
        # 重複を確認するために、平均 O(1) で検索可能な set（集合）を使用します。
        seen = set()
        
        for num in nums:
            # If the number is already in the set, we found a duplicate.
            # すでに集合に含まれている場合は、重複が見つかったことになります。
            if num in seen:
                return True
            # Add the current number to the set.
            # 現在の数値を集合に追加します。
            seen.add(num)
            
        # If the loop finishes without finding a duplicate, return False.
        # ループが終了しても重複が見つからなければ False を返します。
        return False
