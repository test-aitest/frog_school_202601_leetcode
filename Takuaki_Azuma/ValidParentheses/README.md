# Valid Parentheses (No. 20)

### 1. Problem Overview (問題の概要)
Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

'('、')'、'{'、'}'、'['、']' の文字のみを含む文字列 `s` が与えられたとき、その文字列が有効かどうかを判定してください。

以下の条件を満たす場合、入力文字列は有効です：
1. 開いた括弧は、同じ種類の括弧で閉じなければなりません。
2. 開いた括弧は、正しい順序で閉じなければなりません。
3. すべての閉じた括弧には、対応する同じ種類の開いた括弧が必要です。

### Example 1:
**Input:** s = "()"
**Output:** true

### Example 2:
**Input:** s = "()[]{}"
**Output:** true

### Example 3:
**Input:** s = "(]"
**Output:** false
