"""
LRU Cache実装 - OrderedDictを使った方法

この実装はPythonの標準ライブラリcollections.OrderedDictを活用します。
OrderedDictは挿入順序を保持する辞書で、O(1)で操作できます。
"""

from collections import OrderedDict


class LRUCache:
    """
    Least Recently Used (LRU) Cacheの実装
    
    容量制限付きのキャッシュで、最も古く使われた要素を自動的に削除します。
    """
    
    def __init__(self, capacity: int):
        """
        初期化
        
        Args:
            capacity: キャッシュの最大容量（正の整数）
        
        注意点:
            - OrderedDictは挿入順序を保持します
            - 最後に追加/アクセスした要素が末尾に来ます
            - 先頭の要素が最も古い（削除候補）要素です
        """
        self.capacity = capacity
        # OrderedDictを初期化
        # この辞書は {key: value} の形式でデータを保持します
        self.cache = OrderedDict()
    
    def get(self, key: int) -> int:
        """
        キーに対応する値を取得
        
        Args:
            key: 取得したいキー
        
        Returns:
            キーが存在する場合: 対応する値
            キーが存在しない場合: -1
        
        アルゴリズム:
            1. キーが存在するかチェック
            2. 存在する場合:
               - 値を取得
               - そのキーを辞書の最後に移動（最近使用したことを示す）
               - 値を返す
            3. 存在しない場合: -1を返す
        
        時間計算量: O(1)
        """
        if key not in self.cache:
            return -1
        
        # キーを最後に移動（最近使用したことを示す）
        # move_to_end()はO(1)で実行されます
        self.cache.move_to_end(key)
        
        # 値を返す
        return self.cache[key]
    
    def put(self, key: int, value: int) -> None:
        """
        キー・バリューペアを追加または更新
        
        Args:
            key: 追加/更新したいキー
            value: 対応する値
        
        アルゴリズム:
            1. キーが既に存在する場合:
               - 値を更新
               - そのキーを最後に移動（最近使用したことを示す）
            2. キーが存在しない場合:
               - 新しいキー・バリューペアを追加
               - 容量を超えている場合、最も古い要素（先頭）を削除
        
        時間計算量: O(1)
        """
        if key in self.cache:
            # キーが既に存在する場合: 値を更新して最後に移動
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            # 新しいキーを追加
            self.cache[key] = value
            
            # 容量を超えている場合、最も古い要素を削除
            # popitem(last=False)は先頭（最も古い）要素を削除します
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)


# 使用例とテスト
if __name__ == "__main__":
    print("=== LRU Cache テスト ===\n")
    
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

