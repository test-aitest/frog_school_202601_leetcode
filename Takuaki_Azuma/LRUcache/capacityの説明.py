"""
capacityについて理解する

LRU Cacheのcapacityは、ポルシェの例で言うと「エンジンの排気量」や「座席数」のようなものです。
"""

class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        """
        capacity: キャッシュの最大容量（スペックの1つ）
        
        ポルシェの例で言うと:
        - capacity = 2 → 座席数2席のポルシェ
        - capacity = 5 → 座席数5席のポルシェ
        
        LRU Cacheの場合:
        - capacity = 2 → 最大2個のキー・バリューペアを保存できる
        - capacity = 5 → 最大5個のキー・バリューペアを保存できる
        """
        # capacityは引数として受け取る（スペック）
        # self.capacityはインスタンス変数として保存（このオブジェクトの属性）
        self.capacity = capacity
        
        # 他のパーツも準備
        self.cache = {}
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head
    
    def _remove(self, node: Node) -> None:
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
    
    def _insert(self, node: Node) -> None:
        prev, next = self.tail.prev, self.tail
        node.next, node.prev = next, prev
        prev.next = next.prev = node
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            oldest_node = self.head.next
            self._remove(oldest_node)
            del self.cache[oldest_node.key]


# ============================================
# capacityの違いを理解する
# ============================================

print("=" * 60)
print("capacity = 2 のキャッシュを作る")
print("=" * 60)

# capacity = 2 のキャッシュ1号機を作る
cache1 = LRUCache(2)  # ← capacity = 2 を指定
print(f"cache1の容量: {cache1.capacity}")  # 2

# 2個まで保存できる
cache1.put(1, 10)
cache1.put(2, 20)
print("✅ 2個まで保存できました")

# 3個目を追加すると、最も古い1が削除される
cache1.put(3, 30)
print(f"get(1) = {cache1.get(1)}")  # -1（削除された）
print(f"get(2) = {cache1.get(2)}")  # 20
print(f"get(3) = {cache1.get(3)}")  # 30

print("\n" + "=" * 60)
print("capacity = 5 のキャッシュを作る")
print("=" * 60)

# capacity = 5 のキャッシュ2号機を作る
cache2 = LRUCache(5)  # ← capacity = 5 を指定
print(f"cache2の容量: {cache2.capacity}")  # 5

# 5個まで保存できる
for i in range(1, 6):
    cache2.put(i, i * 10)
    print(f"  {i}を追加")

print("\n5個まで保存できました！")
print(f"get(1) = {cache2.get(1)}")  # 10（まだ残っている）
print(f"get(5) = {cache2.get(5)}")  # 50

# 6個目を追加すると、最も古い1が削除される
cache2.put(6, 60)
print(f"\n6個目を追加 → get(1) = {cache2.get(1)}")  # -1（削除された）

print("\n" + "=" * 60)
print("【まとめ】")
print("=" * 60)
print("✅ capacity = 引数（スペックを指定する）")
print("✅ self.capacity = インスタンス変数（このオブジェクトの属性）")
print("✅ capacityの値によって、保存できる最大個数が決まる")
print("\n")
print("cache1: capacity = 2 → 最大2個まで保存")
print("cache2: capacity = 5 → 最大5個まで保存")

