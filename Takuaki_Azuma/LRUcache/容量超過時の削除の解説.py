"""
容量超過時の削除処理の解説 / Explanation of Eviction When Capacity Exceeded

この部分は、put操作で容量を超えた時に最も古いノードを削除する処理です。
This part handles removing the oldest node when capacity is exceeded during put operation.
"""

class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # {key: Node} のマッピング
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove_node(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _pop_head(self) -> Node:
        """最も古いノード（headの次）を削除して返す"""
        first_node = self.head.next
        self._remove_node(first_node)
        return first_node
    
    def put(self, key: int, value: int) -> None:
        # ... 省略 ...
        
        # 容量を超えている場合、最も古いノードを削除
        if len(self.cache) > self.capacity:
            oldest_node = self._pop_head()
            del self.cache[oldest_node.key]


# ============================================
# 詳しい解説 / Detailed Explanation
# ============================================

print("=" * 60)
print("容量超過時の削除処理 / Eviction When Capacity Exceeded")
print("=" * 60)

print("""
【コードの場所 / Code Location】
putメソッド内の最後の部分です。
This is the final part of the put method.

【処理の流れ / Process Flow】
1. 新しいノードを追加した後
2. 容量をチェック
3. 容量超過なら最も古いノードを削除
""")

print("\n" + "=" * 60)
print("【ステップ1: 容量チェック / Step 1: Capacity Check】")
print("=" * 60)

print("""
if len(self.cache) > self.capacity:
    # 削除処理

【意味 / Meaning】
- len(self.cache): 現在のキャッシュ内の要素数
- self.capacity: キャッシュの最大容量
- 要素数が容量を超えているかチェック

【例 / Example】
capacity = 2 の場合:
- 要素数が2以下 → 削除不要
- 要素数が3以上 → 削除が必要
""")

print("\n" + "=" * 60)
print("【ステップ2: 最も古いノードを取得 / Step 2: Get Oldest Node】")
print("=" * 60)

print("""
oldest_node = self._pop_head()

【_pop_head()の動作 / How _pop_head() Works】
1. head.next を取得（最も古いノード）
2. そのノードを連結リストから削除
3. 削除したノードを返す

【視覚的に / Visually】
Before:
head <-> [Node(1)] <-> [Node(2)] <-> [Node(3)] <-> tail
          ↑
      最も古い

After _pop_head():
head <-> [Node(2)] <-> [Node(3)] <-> tail
          ↑
      新しい最も古い
""")

print("\n" + "=" * 60)
print("【ステップ3: ハッシュマップから削除 / Step 3: Remove from Hash Map】")
print("=" * 60)

print("""
del self.cache[oldest_node.key]

【なぜ必要？ / Why Needed?】
- _pop_head()は連結リストから削除するだけ
- ハッシュマップ（self.cache）からも削除する必要がある
- そうしないと、get()で古いノードにアクセスできてしまう

【2つのデータ構造から削除 / Remove from Both Data Structures】
1. 連結リストから削除: _pop_head()で実行済み
2. ハッシュマップから削除: del self.cache[key]で実行
""")

print("\n" + "=" * 60)
print("【実際の動作例 / Actual Example】")
print("=" * 60)

print("""
capacity = 2 のキャッシュで:

1. put(1, 10)
   cache = {1: Node(1,10)}
   連結リスト: head <-> [Node(1)] <-> tail
   len(cache) = 1 <= capacity(2) → 削除不要

2. put(2, 20)
   cache = {1: Node(1,10), 2: Node(2,20)}
   連結リスト: head <-> [Node(1)] <-> [Node(2)] <-> tail
   len(cache) = 2 <= capacity(2) → 削除不要

3. put(3, 30) ← ここで容量超過！
   cache = {1: Node(1,10), 2: Node(2,20), 3: Node(3,30)}
   len(cache) = 3 > capacity(2) → 削除が必要！
   
   【削除処理 / Eviction Process】
   a. oldest_node = _pop_head() → Node(1,10)を取得
   b. 連結リストから削除:
      head <-> [Node(2)] <-> [Node(3)] <-> tail
   c. del self.cache[1] → ハッシュマップからも削除
   
   結果:
   cache = {2: Node(2,20), 3: Node(3,30)}
   連結リスト: head <-> [Node(2)] <-> [Node(3)] <-> tail
""")

print("\n" + "=" * 60)
print("【なぜ2つの削除が必要？ / Why Two Deletions?】")
print("=" * 60)

print("""
LRU Cacheは2つのデータ構造を使っています:

1. ハッシュマップ (self.cache)
   - キーからノードへのO(1)アクセス
   - {key: Node} の形式

2. 双方向連結リスト (head <-> ... <-> tail)
   - 使用順序を管理
   - 最も古い = head.next
   - 最も新しい = tail.prev

【削除の必要性 / Need for Deletion】
- 連結リストから削除しないと:
  → 順序が正しく管理されない
  → 古いノードが残り続ける

- ハッシュマップから削除しないと:
  → get(key)で古いノードにアクセスできてしまう
  → メモリリーク（memory leak）の原因
""")

print("\n" + "=" * 60)
print("【コードの流れ / Code Flow】")
print("=" * 60)

print("""
put(key, value)の全体の流れ:

1. キーが既に存在する場合:
   - 値を更新
   - 末尾に移動（最近使用）

2. キーが存在しない場合:
   a. 新しいノードを作成
   b. ハッシュマップに追加: self.cache[key] = new_node
   c. 連結リストに追加: self._add_node(new_node)
   
   d. 【ここ！】容量チェック:
      if len(self.cache) > self.capacity:
          oldest_node = self._pop_head()  # 連結リストから削除
          del self.cache[oldest_node.key]  # ハッシュマップから削除
""")

print("\n" + "=" * 60)
print("【重要なポイント / Key Points】")
print("=" * 60)

print("""
✅ 容量チェックは追加「後」に行う
   → 追加してから容量を超えたかチェック

✅ 2つのデータ構造から削除する
   → 連結リスト: _pop_head()で削除
   → ハッシュマップ: del self.cache[key]で削除

✅ 最も古いノード = head.next
   → 常にheadの次が最も古い要素

✅ O(1)で実行可能
   → _pop_head()はO(1)
   → del操作もO(1)
""")

print("\n" + "=" * 60)
print("【まとめ / Summary】")
print("=" * 60)
print("✅ 容量超過時に最も古いノードを削除")
print("✅ 連結リストとハッシュマップの両方から削除")
print("✅ 容量を維持してLRU Cacheの動作を保証")
print("\n")
print("✅ Removes oldest node when capacity exceeded")
print("✅ Removes from both linked list and hash map")
print("✅ Maintains capacity and ensures LRU Cache works correctly")


