"""
_add_nodeメソッドの詳しい解説 / Detailed Explanation of _add_node Method

_add_nodeは、ノードを連結リストの末尾（tailの前）に追加するメソッドです。
_add_node is a method that adds a node to the end of the linked list (before tail).
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
        self.cache = {}
        self.head = Node()  # ダミーノード
        self.tail = Node()  # ダミーノード
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, node: Node) -> None:
        """
        ノードを連結リストの末尾（tailの前）に追加
        
        Add node to the end of the linked list (before tail)
        
        これは「最近使用した」ことを示します。
        This indicates "recently used".
        """
        # tailの前のノード（現在最も新しい要素）
        # Node before tail (currently newest element)
        prev_node = self.tail.prev
        
        # 新しいノードを挿入
        # Insert new node
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node


# ============================================
# ステップバイステップで理解する
# ============================================

print("=" * 60)
print("_add_nodeメソッドの動作 / How _add_node Works")
print("=" * 60)

print("\n【初期状態 / Initial State】")
print("head <-> tail")
print("  ↑      ↑")
print(" prev   next")

print("\n【ステップ1: ノード1を追加 / Step 1: Add Node 1】")
print("追加前 / Before:")
print("head <-> tail")
print("\n_add_node(Node(1, 10))を実行 / Execute _add_node(Node(1, 10))")

# 実際の動作をシミュレート
head = Node()
tail = Node()
head.next = tail
tail.prev = head

print("\n1. prev_node = tail.prev を取得")
print("   prev_node = head")
prev_node = tail.prev

print("\n2. prev_node.next = node を設定")
print("   head.next = Node(1, 10)")
node1 = Node(1, 10)
prev_node.next = node1

print("\n3. node.prev = prev_node を設定")
print("   Node(1, 10).prev = head")
node1.prev = prev_node

print("\n4. node.next = tail を設定")
print("   Node(1, 10).next = tail")
node1.next = tail

print("\n5. tail.prev = node を設定")
print("   tail.prev = Node(1, 10)")
tail.prev = node1

print("\n追加後 / After:")
print("head <-> [Node(1,10)] <-> tail")
print("  ↑         ↑         ↑")
print(" prev      prev      next")
print(" next      next      prev")

print("\n" + "=" * 60)
print("【ステップ2: ノード2を追加 / Step 2: Add Node 2】")
print("=" * 60)

print("追加前 / Before:")
print("head <-> [Node(1,10)] <-> tail")

print("\n_add_node(Node(2, 20))を実行 / Execute _add_node(Node(2, 20))")

print("\n1. prev_node = tail.prev を取得")
print("   prev_node = Node(1, 10)  ← 現在最も新しい要素")
prev_node = tail.prev  # Node(1, 10)

print("\n2-5. 同じ手順でNode(2, 20)を追加")
node2 = Node(2, 20)
prev_node.next = node2
node2.prev = prev_node
node2.next = tail
tail.prev = node2

print("\n追加後 / After:")
print("head <-> [Node(1,10)] <-> [Node(2,20)] <-> tail")
print("  ↑         ↑              ↑              ↑")
print(" prev      prev           prev           next")
print(" next      next           next           prev")

print("\n" + "=" * 60)
print("【重要なポイント / Key Points】")
print("=" * 60)

print("""
1. なぜ末尾に追加するのか？ / Why add to the end?
   → 末尾 = 最も最近使った要素
   → Tail = Most recently used element
   
2. なぜtailの前なのか？ / Why before tail?
   → tailはダミーノード（実際のデータを持たない）
   → tail is a dummy node (doesn't hold actual data)
   → 実際のデータはtailの前に配置
   → Actual data is placed before tail

3. 4つのポインタを更新する理由 / Why update 4 pointers?
   → 双方向連結リストなので、前後両方のリンクが必要
   → Doubly linked list needs links in both directions
   → prev_node.next と node.prev を接続
   → node.next と tail.prev を接続
   → Connect prev_node.next and node.prev
   → Connect node.next and tail.prev
""")

print("\n" + "=" * 60)
print("【視覚的な理解 / Visual Understanding】")
print("=" * 60)

print("""
_add_node(node)の動作:

【Before】
head <-> [A] <-> [B] <-> tail
                    ↑
              現在の末尾

【After _add_node([C])】
head <-> [A] <-> [B] <-> [C] <-> tail
                            ↑
                        新しい末尾

手順:
1. prev_node = tail.prev  (Bを取得)
2. prev_node.next = node  (B.next = C)
3. node.prev = prev_node  (C.prev = B)
4. node.next = tail       (C.next = tail)
5. tail.prev = node       (tail.prev = C)
""")

print("\n" + "=" * 60)
print("【実際のコードで確認 / Verify with Actual Code】")
print("=" * 60)

cache = LRUCache(3)

print("\n1. Node(1, 10)を追加:")
cache._add_node(Node(1, 10))
print(f"   連結リスト: head <-> [Node(1,10)] <-> tail")
print(f"   head.next.key = {cache.head.next.key}")
print(f"   tail.prev.key = {cache.tail.prev.key}")

print("\n2. Node(2, 20)を追加:")
cache._add_node(Node(2, 20))
print(f"   連結リスト: head <-> [Node(1,10)] <-> [Node(2,20)] <-> tail")
print(f"   head.next.key = {cache.head.next.key}")
print(f"   tail.prev.key = {cache.tail.prev.key}")

print("\n3. Node(3, 30)を追加:")
cache._add_node(Node(3, 30))
print(f"   連結リスト: head <-> [Node(1,10)] <-> [Node(2,20)] <-> [Node(3,30)] <-> tail")
print(f"   head.next.key = {cache.head.next.key} (最も古い)")
print(f"   tail.prev.key = {cache.tail.prev.key} (最も新しい)")

print("\n" + "=" * 60)
print("【まとめ / Summary】")
print("=" * 60)
print("✅ _add_nodeは末尾（tailの前）にノードを追加")
print("✅ 4つのポインタを更新して双方向リンクを維持")
print("✅ 末尾 = 最も最近使った要素")
print("✅ O(1)の時間計算量で実行可能")
print("\n")
print("✅ _add_node adds node to end (before tail)")
print("✅ Updates 4 pointers to maintain bidirectional links")
print("✅ Tail = Most recently used element")
print("✅ Executes in O(1) time complexity")


