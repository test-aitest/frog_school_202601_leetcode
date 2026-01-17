# Best Time to Buy and Sell Stock (No. 121)

## 1. Problem Overview (問題の概要)
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`-th day.
You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

ある銘柄の `i` 日目の価格が `prices[i]` で与えられる配列 `prices` があります。
**ある1日**を選んで株式を買い、**その後の別の日**を選んで売ることで、利益を最大化したいと考えています。
この取引から得られる最大利益を返してください。利益が得られない場合は 0 を返してください。

**Example 1:**
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

## 2. Key Vocabulary & Phrases (重要な語彙と表現)
- **Maximize profit**: 利益を最大化する
- **Transaction**: 取引
- **i-th day**: i番目の日
- **In the future**: 未来に（後の日付で）

## 3. Approach & Intuition (アプローチと直感)
To maximize profit, we need to find the largest difference between a selling price and a buying price, strictly with the buying day occurring *before* the selling day.
(利益を最大化するには、売り値と買い値の差が最大になる組み合わせを見つける必要があります。ただし、買う日は売る日より*前*でなければなりません。)

We can iterate through the list of prices while keeping track of the **minimum price so far** (lowest buying price). At each step, we calculate the potential profit if we sold at the current price.
(価格リストを走査しながら、**これまでの最安値**（最も低い買い値）を記録し続けます。各ステップで、現在の価格で売った場合の潜在的な利益を計算します。)

## 4. Code Implementation (実装)
See `solution.py` for the implementation.

## 5. Complexity Analysis (計算量解析)
- **Time Complexity**: O(n) - We only traverse the list once.
- **Space Complexity**: O(1) - We only use a few variables for tracking max profit and min price.
