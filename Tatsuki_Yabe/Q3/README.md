# [881.] [Boats to Save People] (Medium)

## 🔗 Problem Link

[LeetCode Link Here](https://leetcode.com/problems/boats-to-save-people/description/)

## 💡 Problem Summary

We are given an array of integers representing people's weights and integer representing the weight limit of a boat. Each boat can carry at most two people at the same time, provided their combined weight is less than or equal to the limit. We need to find the minimum number of boats required to save everyone

[AI 添削前の添削後]

<details>
  <summary>AI添削前</summary>
  We are given an array of non-negative integers representing the weight of the person, and the number representing the limit each boat can carry. We can prepare an infinite number of boats, but if each boat carried at most two people at the same time, how many boats should we prepare at least?
</details>

**Constraints:**

- $1 \leq people.length \leq 5*10^4$
- $1 \leq people[i] \leq limit \leq 3*10^4$

## 🧐 Approach & Intuition

### Check Constraints

First, we should check the constraints. Specifically, we must recognize that $people[i] \le limit$, which guarantees that every person fits in a boat alone. I initially missed the context, but naturally, we have to read the problem statement carefully to fully understand the scenario.

<details>
  <summary>AI添削前</summary>
  At first, We should check the constraints. Especially, we have to recognize the fact that "personal weight is much less than the limit of the boat🤣". I could not notice such constraint because I didn't understand the context of this problem. [当然のことながら、]We have to read given question respectivitly[丁寧に] and understand the situation the question says.

[have to と must の使い分け???]

</details>

### Initial Thought

The optimal strategy is to pair the heaviest person with the lightest person whenever possible. To do this, we must first sort the array in ascending order.

Then, we use a Two Pointer approach. We compare the sum of the lightest person (people[left]) and the heaviest person (people[right]) with the limit.

- If people[left] + people[right] <= limit, both can share a boat. We move both pointers inward
- If the sum exceeds the limit, the heaviest person is too heavy to share with the lightest one. The heaviest person takes a boat alone, and we only move the right pointer.

This process continues until the two pointers meet.

<details>
  <summary>AI添削前</summary>
  The optimised combination of the candidate is the number who is lightest and who is heaviest in the array, so we must sort the array at first to arrange [昇順に並べるために]. The we continue the comparison between the sum of the candidates' weight and given limit. If the limit was bigger, both of them can ride a boat and we can move the right and left pointer position. However if the sum was bigger, we would prepare a boat for the heaviest person, so we can move only right pointer position. If the right pointer We continue advancing i as long as right_pointer > left_pointer, and if the right_pointer was less than left_pointer, return the boat number.
</details>

#### Algorithm Detail

The code logic follows the steps:

- 1, **Sort the Array**
  Sorted the people array in ascending order.

- 2, **Initialize Variable**
  Define the pointers:[left] at the beginning(0) and pointers:[right] at the end(people.lemgth - 1). Also, initialize a [boats] counter.

- 3, **Loop**
  Iterate while left <= right

  - If people[left] + people[right] <= limit:
    - Increment left pointer (left += 1)
    - Decrement right pointer (right -= 1)
    - Increment boats counter (boats += 1)

  <details>
  <summary>AI添削前</summary>
  If the limit is bigger than the sum of the lightest and heaviest persons, the pointers update.
  </details>

- 4, **Return the Number of the Boats**
  Return the total number of the boats.
