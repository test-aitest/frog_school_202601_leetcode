package main

func isSubsequence(s string, t string) bool {
	slen := len(s)
	var point int
	for i := range t {
		if point == slen {
			break
		}
		if t[i] == s[point] {
			point++
		}
	}
	return slen == point
}

/*
## Solution
The goal is to determine if string `s` is a subsequence of string `t`.
A subsequence maintains the original relative order of characters but allows for some characters to be skipped.

## Approach (Two Pointers / Greedy)
We can solve this efficiently using a two-pointer approach to scan both strings.
- We use `i` to iterate through the target string `t`.
- We use `point` as a pointer for the source string `s`.

By iterating through `t` once, we greedily match characters from `s`. If we find a match, we move the pointer `point` to the next character in `s`.

## Algorithm
1. Initialize `point` to 0 to track our progress in string `s`.
2. Iterate through string `t` using a loop:
   - If `point` equals the length of `s`, it means all characters have been matched; we can exit the loop early.
   - If the current character in `t` matches `s[point]`, increment `point`.
3. After the loop, check if `point` is equal to the length of `s`.
   - If they are equal, `s` is a subsequence of `t`.

## Why This Works
This "greedy" approach works because if a character in `s` can be matched at an earlier position in `t`, it leaves more characters in `t` available for subsequent matches in `s`. This ensures we find the subsequence if it exists.

## Complexity Analysis
### Space Complexity: O(1)
We only use a few integer variables regardless of the input size.

### Time Complexity: O(n)
Where `n` is the length of string `t`. We perform a single pass through `t`.
*/
