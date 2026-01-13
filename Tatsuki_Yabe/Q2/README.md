# [941.] [Valid Mountain Array] (Easy)

## 🔗 Problem Link

[LeetCode Link Here](https://leetcode.com/problems/valid-mountain-array/description/)

## 💡 Problem Summary

We are given an array of non-negative integers. We must determine if the array is a valid mountaion array. Amountain array is defied by a strictly increasing sequence followed by a strictly decreasing sequence.

<details>
  <summary>AI添削前</summary>
  We are given an array of non-negative integers. We must find an array that satisfies specific conditions and return true or false. This condition is that the array has strict increased sub-array and strict decreased sub-array, looks like a mountain.
</details>

**Constraints:**

- $1 \leq arr.length \leq 10^4$
- $0 \leq arr[i] \leq 10^4$

## 🧐 Approach & Intuition

### Initial Thought

I focused on comparing adjacent elements. First, we expect the numbers to be strictly increasing, so we advance the index i as long as arr[i] < arr[i+1]. After reaching the peak, we must check for a strictly decreasing sequence. We continue advancing i as long as arr[i] > arr[i+1]. If the index reaches the end of the array after these two steps, the sequence is valid.

<details>
  <summary>AI添削前</summary>
  I considered the comparison of the sequential two numbers in the array.
First we expect the strict increasing, so the index i was increased if the array[i+1] is bigger than array[i]. After that we must check the strict decreasing in the array, so the index i was increased if the array[i] is bigger that array[i+1]. If the index is equal to the length of the array, the sequance is finished
</details>

#### Algorism Detail

The code logic follows the steps:

- 1, **Initialize Pointer**
  I used a pointer(index i) starting from beginning of the array to track the current position.

- 2, **Iterate the strict increasing**
  Continue to increment the pointer while the sequence is strictly increasing.

- 3, **Check Peak Validity**
  If the pointer hasn't moved(the start is not increasing) or if it has already reached the end(no department part), return false.

  <details>
  <summary>AI添削前</summary>
  If you cannot find the strict increasing or reached the end of the number in the array, return false.
  </details>

- 4, **Iterate the strict decreasing**
  Continue to increment the pointer while sequence is strictly decreasing.

- 5, **Return Result**
  If the pointer has reached the exact end of the array, return false
