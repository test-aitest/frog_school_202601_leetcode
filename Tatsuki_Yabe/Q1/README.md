# [11. ] [Container With Most Water] (Medium)

## 🔗 Problem Link

[LeetCode Link Here](https://leetcode.com/problems/container-with-most-water/description/)

## 💡 Problem Summary

We are given an array of non-negative integers representing heights of vertical lines. We must find two lines that form a container with the x-axis to hold the maximum amount of water.
The container's area is determined by the shorter line's height multiplied by the the distance between the two lines.
We return the largest area without spilling water in the container.

## 🧐 Approach & Intuition

### 1. Initial Thought (Brute Force)

I initially considered iterating through all possible combinations. However, this results in a time complexity of $O(n^2)$, so I thought this is not optimized approach.

### 2. Optimization Strategy

To optimize the solution, I decided to use a **[Two Pointer Approach]**
This is the approach we start at edges of the array and keep the length between the edges shortened until the length is equal to 0.
the time complexity is $O(n)$, so this approach is more efficient than Brute Force strategy.

#### Algorism Detail

The code logic follows the steps:
- 1, **Initialize Pointer**
 Set a left pointer at index 0(the beginning of the array) and right pointer at index n-1(the end of the array)
- 2, **Initialize Max Area and calcurate current area**
 Create a variable "maxarea" to store maximum water capacity, which you can calcurate current area between left pointer and right pointer.
- 3, **Loop**
 Continue to move the pointer while left < right and update maxarea. If the width was decreased, the height would be increased to maximize the area.
- 4, **Return**
 Once the pointers meet, return maxarea
