class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # とりあえず解いてみる
        # 集合型のlengthで重複チェック
        return len(nums) != len(set(nums))