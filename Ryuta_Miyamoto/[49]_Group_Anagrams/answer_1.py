#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a hashmap...説明むずい
        ans = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)
            
        return list(ans.values())
# @lc code=end

