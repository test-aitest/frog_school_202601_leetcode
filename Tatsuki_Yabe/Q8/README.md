# [268.] [Missing Number] (Easy)

## 🔗 Problem Link

[LeetCode Link Here](https://leetcode.com/problems/missing-number/description/)

## 💡 Problem Summary

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

<details>
<summary>AI添削前</summary>
Given an array nums containing unique number from 0 to n. You must find the only missing number from the array.
</details>

**Constraints:**

- n == nums.length
- $1 \leq n \leq 10^4$
- $0 \le nums[i] \le n$
- All the numbers of nums are unique.

## 🧐 Approach & Intuition

### 1. Initial Thought (Hash Map Strategy)

I initially considered checking the existence of each number in the range [0, n]. To do so, I planned to use a Hash Map (or a Boolean array) where the key is the number and the value is a boolean flag indicating its presence in the array.
Then, I would iterate through the range 0 to n and check which number's flag is missing (false). However, this requires $O(n)$ space.

<details>
<summary>AI添削前</summary>
I initially considered whether the number in the array is in the range from 0 to n. To do so, I decided to use hashmap which key was number and value was true flag to indicate that it is a number in the array.
Then I searched for the number by the way of assigning each value in the range of 0 to n and checking whether the flag was false(missing number).
</details>

### 2. Gauss Sum

We can use the Gauss Sum formula (Arithmetic Progression) to solve this problem efficiently with $O(1)$ space.The formula states that the sum of the first $n$ positive integers is:$$\text{Sum} = \frac{n(n + 1)}{2}$$By comparing the "Expected Sum" (using the formula) and the "Actual Sum" (sum of elements in the array), the difference between them will be the missing number.

<details>
<summary>AI添削前</summary>
We can use Gauss Sum formula to sole this question. This formula shows that if you sum the subsequencial positive numbers, the total is a number that the multiplied of first number and last number in the range of 1 to n divided by 2.
</details>

### Algorism Detail

The code logic follws these steps:

- 1, **Identify $n$**
  Get the length of the given array, which represents n.
- 2, **Calculate Expected Sum**
  Calculate the sum of all integers from 0 to n using the Gauss Sum formula: n \* (n + 1) / 2.

    <details>
    <summary>AI添削前</summary>
    Use Gauss Sum formula and this answer is intended sum.
    </details>

- 3, **Calculate Actual Sum**
  Iterate through the nums array and calculate the sum of all its elements.

  <details>
    <summary>AI添削前</summary>
    Sum all the numbers in the given array and this answer is actual sum.
    </details>

- 4, **Return the Result**
  Subtract the Actual Sum from the Expected Sum. The result is the missing number.
