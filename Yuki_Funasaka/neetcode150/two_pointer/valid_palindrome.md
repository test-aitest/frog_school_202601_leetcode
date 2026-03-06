# Valid Palindrome
# Understand Match
## question
- Given a string s. Is this ASCII or not? Should we concern about others for example emoji?
- Given a string s. What does this contain, uppercase and lowercase alphabet and interger?
- How should we handle spaces and non-alphabet?

## happy path
- s = "lol", true
- s = "lolo" false
- s = " l ! o ! l " true

## edge case
- s = "" true
- s = "s" true
- s = " " true

## constraints
How many characters does string s contain at least and at most? What's range?

# Plan
This is a Two Pointers problem.
We can use classic two pointer approach moving from both ends to the center.

### BF
The brute force approach would be to first clean the string.
And validate if the string is alphanumeric, convert to lower case.
Finally, we check if the cleaned string equals its reverse.

```
clean = []
for c in s:
    if c.isalnum():
        clean.append(c.lower())

return clean == clean[::-1]
```
This works in O(n) time complexity. And Space complexity is also O(n).
It's using an extra memory. If possible, we want to work this in O(n) space complexity.
That's where two pointer moving from both right and left end to the center.

### Two pointer
```
l, r = 0, len(s)

while l < r:
    if not s[l].isalnum():
        l += 1
        continue
    if not s[r].isalnum():
        r -= 1
        continue
    # both is alphanum
    if s[l].lower() != s[r].lower():
        return False
    l += 1
    r -= 1
```

# Implement
# Review Evaluate

```python

```