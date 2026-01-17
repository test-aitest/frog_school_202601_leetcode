"""
LRU Cache実装 - 双方向連結リストを使った方法

この実装は基本的なデータ構造を組み合わせてLRU Cacheを実装します。
アルゴリズムの理解を深めるのに最適です。

データ構造:
    - ハッシュマップ (dict): キーからノードへのO(1)アクセス
    - 双方向連結リスト: 使用順序を管理（先頭=最も古い、末尾=最も新しい）
"""


class Node:
    """
    双方向連結リストのノード
    
    各ノードは以下の情報を持ちます:
        - key: キャッシュのキー
        - value: キャッシュの値
        - prev: 前のノードへの参照
        - next: 次のノードへの参照
    """
    
    def __init__(self, key: int = 0, value: int = 0):
        """
        ノードの初期化
        
        Args:
            key: キャッシュのキー
            value: キャッシュの値
        """
        self.key = key
        self.value = value
        self.prev = None  # 前のノード
        self.next = None  # 次のノード


class LRUCache:
    """
    Least Recently Used (LRU) Cacheの実装
    
    双方向連結リストとハッシュマップを組み合わせて実装します。
    
    構造:
        head <-> node1 <-> node2 <-> ... <-> tail
        (headの次が最も古い要素、tailの前が最も新しい要素)
    """
    
    def __init__(self, capacity: int):
        """
        初期化
        
        Args:
            capacity: キャッシュの最大容量
        
        設計:
            - headとtailはダミーノード（実際のデータは持たない）
            - これにより、境界条件の処理が簡単になります
            - cache: キーからノードへのマッピング（O(1)アクセス用）
        """
        self.capacity = capacity
        self.cache = {}  # {key: Node} の形式
        
        # ダミーノードを作成（境界処理を簡単にするため）
        self.head = Node()  # 最も古い要素の前
        self.tail = Node()  # 最も新しい要素の後
        
        # headとtailを連結
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, node: Node) -> None:
        """
        ノードを連結リストの末尾（tailの前）に追加
        
        これは「最近使用した」ことを示します。
        
        Args:
            node: 追加するノード
        
        アルゴリズム:
            1. tailの前のノードを取得
            2. そのノードとtailの間に新しいノードを挿入
            3. ポインタを適切に更新
        
        時間計算量: O(1)
        """
        # tailの前のノード（現在最も新しい要素）
        prev_node = self.tail.prev
        
        # 新しいノードを挿入
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node
    
    def _remove_node(self, node: Node) -> None:
        """
        ノードを連結リストから削除
        
        Args:
            node: 削除するノード
        
        アルゴリズム:
            1. ノードの前後のポインタを更新
            2. ノード自体のポインタは残しておく（再利用可能）
        
        時間計算量: O(1)
        """
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _move_to_end(self, node: Node) -> None:
        """
        ノードを末尾に移動（最近使用したことを示す）
        
        Args:
            node: 移動するノード
        
        アルゴリズム:
            1. ノードを現在の位置から削除
            2. 末尾に追加
        
        時間計算量: O(1)
        """
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_head(self) -> Node:
        """
        最も古いノード（headの次）を削除して返す
        
        Returns:
            削除されたノード
        
        時間計算量: O(1)
        """
        first_node = self.head.next
        self._remove_node(first_node)
        return first_node
    
    def get(self, key: int) -> int:
        """
        キーに対応する値を取得
        
        Args:
            key: 取得したいキー
        
        Returns:
            キーが存在する場合: 対応する値
            キーが存在しない場合: -1
        
        アルゴリズム:
            1. ハッシュマップでキーを検索（O(1)）
            2. ノードが見つかった場合:
               - 値を取得
               - ノードを末尾に移動（最近使用したことを示す）
               - 値を返す
            3. 見つからない場合: -1を返す
        
        時間計算量: O(1)
        """
        node = self.cache.get(key)
        
        if not node:
            return -1
        
        # ノードを末尾に移動（最近使用したことを示す）
        self._move_to_end(node)
        
        return node.value
    
    def put(self, key: int, value: int) -> None:
        """
        キー・バリューペアを追加または更新
        
        Args:
            key: 追加/更新したいキー
            value: 対応する値
        
        アルゴリズム:
            1. キーが既に存在する場合:
               - ノードの値を更新
               - ノードを末尾に移動（最近使用したことを示す）
            2. キーが存在しない場合:
               - 新しいノードを作成
               - ハッシュマップに追加
               - 連結リストの末尾に追加
               - 容量を超えている場合:
                 * 最も古いノード（headの次）を削除
                 * ハッシュマップからも削除
        
        時間計算量: O(1)
        """
        node = self.cache.get(key)
        
        if node:
            # キーが既に存在する場合: 値を更新して末尾に移動
            node.value = value
            self._move_to_end(node)
        else:
            # 新しいキーを追加
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            
            # 容量を超えている場合、最も古いノードを削除
            if len(self.cache) > self.capacity:
                oldest_node = self._pop_head()
                del self.cache[oldest_node.key]


# 使用例とテスト
if __name__ == "__main__":
    print("=== LRU Cache テスト (双方向連結リスト版) ===\n")
    
    # 例1: LeetCodeの例題
    print("例1: LeetCodeの例題")
    cache = LRUCache(2)
    
    print(f"cache.put(1, 1) -> cache is {{1=1}}")
    cache.put(1, 1)
    
    print(f"cache.put(2, 2) -> cache is {{1=1, 2=2}}")
    cache.put(2, 2)
    
    print(f"cache.get(1) -> {cache.get(1)} (1が返る)")
    
    print(f"cache.put(3, 3) -> 容量超過、2が削除され、cache is {{1=1, 3=3}}")
    cache.put(3, 3)
    
    print(f"cache.get(2) -> {cache.get(2)} (-1が返る、2は削除済み)")
    
    print(f"cache.put(4, 4) -> 容量超過、1が削除され、cache is {{3=3, 4=4}}")
    cache.put(4, 4)
    
    print(f"cache.get(1) -> {cache.get(1)} (-1が返る、1は削除済み)")
    print(f"cache.get(3) -> {cache.get(3)} (3が返る)")
    print(f"cache.get(4) -> {cache.get(4)} (4が返る)")
    
    print("\n" + "="*50 + "\n")
    
    # 例2: より複雑な例
    print("例2: より複雑な例")
    cache2 = LRUCache(3)
    
    operations = [
        ("put", (1, 10), None),
        ("put", (2, 20), None),
        ("put", (3, 30), None),
        ("get", (2,), 20),
        ("put", (4, 40), None),  # 1が削除される
        ("get", (1,), -1),
        ("get", (3,), 30),
        ("get", (4,), 40),
    ]
    
    for op, args, expected in operations:
        if op == "put":
            cache2.put(args[0], args[1])
            print(f"put({args[0]}, {args[1]})")
        elif op == "get":
            result = cache2.get(args[0])
            print(f"get({args[0]}) -> {result} (期待値: {expected})")
            assert result == expected, f"期待値{expected}と異なります: {result}"
    
    print("\n✅ すべてのテストが成功しました！")

