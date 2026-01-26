# [278.] [First Bad Version] (Easy)

## 🔗 Problem Link

[LeetCode Link Here](https://leetcode.com/problems/first-bad-version/description/)

## 💡 Problem Summary

This problem simulates a real-world product management scenario. Suppose you have n versions [1, 2, ..., n] and the latest version failed the quality check. Since each version is developed based on the previous version, all versions after a bad version are also bad.

Your task is to find the first bad version that caused all subsequent versions to fail. An API isBadVersion(version) is provided, and you need to implement a function to find the first bad version while minimizing the number of API calls.

<details>
<summary>AI添削前</summary>
This problem is the real case of the product management. Since your product failed the quality check, you must change the version.

Your task is to find out the first bad version in all version. The version checker api is prepared, so you implement the function to find the first bad version.

</details>

**Constraints:**

- $1 \leq bad \leq n \leq $2^{31} - 1$

## 🧐 Approach & Intuition

### The Strategy(Binary Search)

Since the versions are sorted(good versions come first, followed by bad versions), I decided to use the **Binary Search** strategy to narrow down the search space by half each time.

If the middle version is not bad, the first bad version must be among the number strictly greater than the middle number. If the middle version is bad, the first bad version could be this one or one of the earlier versions.

### Algorism Detail

The code logic follws these steps:

- 1, **Initialize Pointers**
  Set a left pointer at 1(the first version) and a right pointer at n(the last version).
- 2, **Iterate to Narrow Down**
  While the left pointer is less than right pointer, do the following,
  - Calcurate the middle version number
  - If the middle version is bad(if an API isBadVersion(mid) is true), the first bad version is at mid or before it.
  - Else, move the left pointer to middle + 1 because the first bad version must be after the middle number.
- 3, **Return the Result**
  When the loop ends(left == right), the left pointer will be pointing to the first bad version, so return left.
