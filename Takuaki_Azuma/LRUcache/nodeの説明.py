"""
Node（ノード）の理解 / Understanding Node

Nodeは連結リストの「箱」のようなものです。
Node is like a "box" in a linked list.
"""

class Node:
    """
    ノード = データを入れる箱 + 他の箱へのリンク
    
    Node = Box for data + Links to other boxes
    """
    def __init__(self, key: int, val: int):
        self.key = key      # データ1: キー
        self.value = val    # データ2: 値
        self.prev = None    # 前の箱へのリンク
        self.next = None    # 次の箱へのリンク


# ============================================
# 例え1: 電車の車両に例える
# ============================================

print("=" * 60)
print("例え1: 電車の車両（Train Car）に例える")
print("=" * 60)

print("""
Node = 電車の1両の車両

各車両には:
- データ（乗客や荷物）= key, value
- 前の車両への連結 = prev
- 次の車両への連結 = next

[車両1] <-> [車両2] <-> [車両3]
  ↑          ↑          ↑
 prev       prev       prev
 next       next       next
""")

print("""
Node = One train car

Each car has:
- Data (passengers/cargo) = key, value
- Link to previous car = prev
- Link to next car = next

[Car 1] <-> [Car 2] <-> [Car 3]
  ↑          ↑          ↑
 prev       prev       prev
 next       next       next
""")

# ============================================
# 例え2: 鎖の輪に例える
# ============================================

print("\n" + "=" * 60)
print("例え2: 鎖の輪（Chain Link）に例える")
print("=" * 60)

print("""
Node = 鎖の1つの輪

各輪には:
- 中身（データ）= key, value
- 前の輪への接続 = prev
- 次の輪への接続 = next

[輪1] <-> [輪2] <-> [輪3]
  ↑        ↑        ↑
 prev     prev     prev
 next     next     next
""")

print("""
Node = One link in a chain

Each link has:
- Content (data) = key, value
- Connection to previous link = prev
- Connection to next link = next

[Link 1] <-> [Link 2] <-> [Link 3]
   ↑          ↑          ↑
 prev        prev       prev
 next        next       next
""")

# ============================================
# 実際のコードで見てみる
# ============================================

print("\n" + "=" * 60)
print("実際のコードで見てみる / See in Actual Code")
print("=" * 60)

# ノードを作成
node1 = Node(1, 10)  # キー1、値10のノード
node2 = Node(2, 20)  # キー2、値20のノード
node3 = Node(3, 30)  # キー3、値30のノード

print("\nノードを作成しました:")
print("node1: key=1, value=10")
print("node2: key=2, value=20")
print("node3: key=3, value=30")

# ノードを連結
node1.next = node2    # node1の次はnode2
node2.prev = node1    # node2の前はnode1
node2.next = node3    # node2の次はnode3
node3.prev = node2    # node3の前はnode2

print("\nノードを連結しました:")
print("node1 <-> node2 <-> node3")

# ノードを辿る
print("\nノードを辿ってみます:")
current = node1
while current:
    print(f"  key={current.key}, value={current.value}")
    current = current.next

# ============================================
# LRU CacheでのNodeの役割
# ============================================

print("\n" + "=" * 60)
print("LRU CacheでのNodeの役割 / Role of Node in LRU Cache")
print("=" * 60)

print("""
LRU Cacheでは、各Nodeが:
1. データを保存: key（キー）とvalue（値）
2. 順序を管理: prev（前）とnext（次）で連結
3. 使用順序を追跡: 最近使ったNodeを末尾に移動

例:
head <-> [Node(1,10)] <-> [Node(2,20)] <-> tail
          ↑                ↑
        最も古い          最も新しい
""")

print("""
In LRU Cache, each Node:
1. Stores data: key and value
2. Manages order: connected by prev and next
3. Tracks usage: move recently used Node to tail

Example:
head <-> [Node(1,10)] <-> [Node(2,20)] <-> tail
          ↑                ↑
        Oldest           Newest
""")

# ============================================
# 双方向連結リストの利点
# ============================================

print("\n" + "=" * 60)
print("双方向連結リストの利点 / Advantages of Doubly Linked List")
print("=" * 60)

print("""
双方向連結リスト（Doubly Linked List）の利点:

1. 前後両方向に移動できる
   - prevで前のノードに移動
   - nextで次のノードに移動

2. ノードの削除が簡単
   - 前後のノードのポインタを更新するだけ
   - O(1)で削除可能

3. 順序の更新が簡単
   - ノードを削除して末尾に再挿入
   - O(1)で順序更新可能
""")

print("""
Advantages of Doubly Linked List:

1. Can move in both directions
   - Move to previous node with prev
   - Move to next node with next

2. Easy node deletion
   - Just update pointers of previous and next nodes
   - O(1) deletion possible

3. Easy order update
   - Remove node and re-insert at tail
   - O(1) order update possible
""")

print("\n" + "=" * 60)
print("【まとめ】")
print("=" * 60)
print("✅ Node = データを入れる箱 + 他の箱へのリンク")
print("✅ 電車の車両や鎖の輪のようなもの")
print("✅ LRU Cacheでは、データと順序の両方を管理")
print("\n")
print("✅ Node = Box for data + Links to other boxes")
print("✅ Like train cars or chain links")
print("✅ In LRU Cache, manages both data and order")


