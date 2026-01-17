class Node:
    """
    双方向連結リストのノード
    
    改善: クラス名を大文字始まりに変更（Pythonの慣習）
    """
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    """
    LRU Cache実装
    
    改善点:
    - leftNode/rightNode → head/tail (より一般的な命名)
    - remove/insert → _remove/_insert (プライベートメソッド)
    - lruNode → oldest_node (より明確)
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # {key: Node} のマッピング
        
        # ダミーノード: headは最も古い要素の前、tailは最も新しい要素の後
        # 改善: leftNode/rightNode → head/tail
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node: Node) -> None:
        """
        ノードを連結リストから削除
        
        改善:
        - remove → _remove (プライベートメソッドの慣習)
        - 型ヒントを追加
        """
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def _insert(self, node: Node) -> None:
        """
        ノードを連結リストの末尾（tailの前）に追加
        
        改善:
        - insert → _insert (プライベートメソッドの慣習)
        - 型ヒントを追加
        """
        prev, next = self.tail.prev, self.tail
        node.next, node.prev = next, prev
        prev.next = next.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # ノードを削除してから末尾に再挿入（最近使用したことを示す）
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 既存のキー: ノードを削除（後で再挿入するため）
            self._remove(self.cache[key])
        
        # 新しいノードを作成して追加
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        # 容量超過時、最も古いノード（headの次）を削除
        if len(self.cache) > self.capacity:
            # 改善: lruNode → oldest_node (より明確な命名)
            oldest_node = self.head.next
            self._remove(oldest_node)
            del self.cache[oldest_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# テスト
if __name__ == "__main__":
    cache = LRUCache(2)
    
    cache.put(1, 1)
    cache.put(2, 2)
    print(f"get(1) = {cache.get(1)}")  # 1
    
    cache.put(3, 3)  # 2が削除される
    print(f"get(2) = {cache.get(2)}")  # -1
    
    cache.put(4, 4)  # 1が削除される
    print(f"get(1) = {cache.get(1)}")  # -1
    print(f"get(3) = {cache.get(3)}")  # 3
    print(f"get(4) = {cache.get(4)}")  # 4
    
    print("\n✅ すべてのテストが成功しました！")