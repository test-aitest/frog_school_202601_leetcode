"""
O(1)の意味を理解する / Understanding O(1)

O(1)は「データ量に関係なく、常に一定時間で処理できる」という意味です。
O(1) means "can process in constant time regardless of data size."
"""

import time
from collections import OrderedDict

# ============================================
# O(1)の例: 辞書（ハッシュマップ）のアクセス
# ============================================

print("=" * 60)
print("O(1)の例: 辞書（Dictionary/Hash Map）のアクセス")
print("=" * 60)

# データ量を変えながら、アクセス時間を測定
for size in [10, 100, 1000, 10000, 100000]:
    # 辞書を作成
    d = {i: i * 10 for i in range(size)}
    
    # 最後の要素にアクセス（O(1)）
    start = time.time()
    value = d[size - 1]  # 辞書のアクセスはO(1)
    end = time.time()
    
    elapsed = (end - start) * 1000000  # マイクロ秒に変換
    print(f"データ量: {size:6d}個 → アクセス時間: {elapsed:.2f}マイクロ秒")
    print(f"  → データ量が{size // 10}倍になっても、時間はほぼ同じ！")

print("\n" + "=" * 60)
print("O(n)の例: リストの線形探索（比較用）")
print("=" * 60)

# 比較: リストの線形探索はO(n)
for size in [10, 100, 1000, 10000]:
    # リストを作成
    lst = list(range(size))
    
    # 最後の要素を探す（O(n) - 最悪の場合）
    start = time.time()
    target = size - 1
    for i, val in enumerate(lst):
        if val == target:
            break
    end = time.time()
    
    elapsed = (end - start) * 1000000
    print(f"データ量: {size:6d}個 → 探索時間: {elapsed:.2f}マイクロ秒")
    print(f"  → データ量が10倍になると、時間も約10倍になる")

print("\n" + "=" * 60)
print("LRU CacheのO(1)操作")
print("=" * 60)

cache = OrderedDict()

# put操作はO(1)
print("put操作（追加）:")
for i in range(5):
    cache[i] = i * 10
    print(f"  put({i}, {i*10}) → O(1)で実行")

# get操作もO(1)
print("\nget操作（取得）:")
for i in range(5):
    value = cache.get(i, -1)
    print(f"  get({i}) = {value} → O(1)で実行")

# move_to_endもO(1)
print("\nmove_to_end操作（順序更新）:")
cache.move_to_end(0)  # 0を最後に移動
print(f"  move_to_end(0) → O(1)で実行")
print(f"  現在の順序: {list(cache.keys())}")

print("\n" + "=" * 60)
print("【まとめ】")
print("=" * 60)
print("✅ O(1) = データ量に関係なく、常に一定時間")
print("✅ O(n) = データ量に比例して時間が増える")
print("✅ LRU Cacheのget/putはO(1) → 高速！")
print("\n")
print("✅ O(1) = Constant time regardless of data size")
print("✅ O(n) = Time increases proportionally with data size")
print("✅ LRU Cache's get/put are O(1) → Fast!")

