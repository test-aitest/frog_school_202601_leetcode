# [283.] [Move Zeroes] (Easy)

## 🔗 Problem Link

[LeetCode Link Here](https://leetcode.com/problems/move-zeroes/description/)

## 💡 Problem Summary

Given an integer array and this contains one or more zeros and non-zero elements. We must move all zeros to the end of the array maintaining the relative positions of others. The important constraint is not to make the copy of the array

<details>
<summary>AI添削前</summary>
Given an integer array nums containing zeroes and non-zero elements, we must move all zeroes to the end of the array while maintaining the relative order of the non-zero elements. The important constraint is that we must do this in-place without making a copy of the array.
</details>

**Constraints:**

- $1 \leq nums.length \leq 10^4$
- $-2^31 \leq nums[i] \leq 2^31 -1$ =>２の 31 乗 - 1

## 🧐 Approach & Intuition

### 1. Initial Thought (Brute Force)

The first approach that easily comes to mind is the **Brute Force**. However, as you know, this results in a time complexity of $O(n^2)$, which is not an optimal solution.

### 2. Optimization Strategy

To optimize the solution, I decided to use a **Two-Pointer approach**(specifically an overwrite and fill method).
The idea is to shift all non-zero numbers to the left side first, and the fill the remaining right side with zeroes.

#### Algorism Detail

The code logic follows these steps:

- 1, **Initialize "Left" Pointer**
  Set a left pointer at index 0(the beginning of the array). This pointer will track the position where the next non-zero element should be placed.
- 2, **Iterate and Overwrite Non-Zero**
  Continue to move to meet non-zero numbers in the nums array and if met,
  - Swap the non-zero number with the number at the left pointer
  - Move left pointer to right by 1

    <details>
  <summary>AI添削前</summary>
  Iterate through each element v in the nums array. Whenever v is not zero:

- Overwrite the element at the left pointer with v (nums[left] = v).
- Increment the left pointer by 1.
</details>

- 3, **Fill the Rest with Zeroes**
  After the loop, all non-zero elements are correctly placed at the beginning of the array. Now we iterate from the current left pointer to the end of the array and set all remaining elements to 0.
