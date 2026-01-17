"""
LRU Cacheの包括的なテストケース

LeetCodeのテストケースと追加のエッジケースを含みます。
"""

import unittest
from lru_cache_ordereddict import LRUCache as LRUCacheOrderedDict
from lru_cache_doubly_linked import LRUCache as LRUCacheDoublyLinked


class TestLRUCacheOrderedDict(unittest.TestCase):
    """OrderedDict版のテスト"""
    
    def test_leetcode_example(self):
        """LeetCodeの例題1"""
        cache = LRUCacheOrderedDict(2)
        
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        
        cache.put(3, 3)  # 2が削除される
        self.assertEqual(cache.get(2), -1)
        
        cache.put(4, 4)  # 1が削除される
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)
    
    def test_update_existing_key(self):
        """既存のキーの値を更新するテスト"""
        cache = LRUCacheOrderedDict(2)
        
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(1, 10)  # 1の値を更新
        
        self.assertEqual(cache.get(1), 10)
        self.assertEqual(cache.get(2), 2)
        
        # 1が最近更新されたので、2が最も古い
        cache.put(3, 3)  # 2が削除される
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), 10)
        self.assertEqual(cache.get(3), 3)
    
    def test_capacity_one(self):
        """容量が1の場合のテスト"""
        cache = LRUCacheOrderedDict(1)
        
        cache.put(1, 1)
        self.assertEqual(cache.get(1), 1)
        
        cache.put(2, 2)  # 1が削除される
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 2)
    
    def test_get_updates_order(self):
        """get操作が順序を更新するテスト"""
        cache = LRUCacheOrderedDict(3)
        
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        
        # 1を取得すると、1が最も最近使われた要素になる
        cache.get(1)
        
        # 4を追加すると、2が削除される（1は最近使われたので残る）
        cache.put(4, 4)
        self.assertEqual(cache.get(1), 1)  # 1は残っている
        self.assertEqual(cache.get(2), -1)  # 2は削除された
        self.assertEqual(cache.get(3), 3)  # 3は残っている
        self.assertEqual(cache.get(4), 4)  # 4は残っている


class TestLRUCacheDoublyLinked(unittest.TestCase):
    """双方向連結リスト版のテスト"""
    
    def test_leetcode_example(self):
        """LeetCodeの例題1"""
        cache = LRUCacheDoublyLinked(2)
        
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        
        cache.put(3, 3)  # 2が削除される
        self.assertEqual(cache.get(2), -1)
        
        cache.put(4, 4)  # 1が削除される
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)
    
    def test_update_existing_key(self):
        """既存のキーの値を更新するテスト"""
        cache = LRUCacheDoublyLinked(2)
        
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(1, 10)  # 1の値を更新
        
        self.assertEqual(cache.get(1), 10)
        self.assertEqual(cache.get(2), 2)
        
        # 1が最近更新されたので、2が最も古い
        cache.put(3, 3)  # 2が削除される
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), 10)
        self.assertEqual(cache.get(3), 3)
    
    def test_capacity_one(self):
        """容量が1の場合のテスト"""
        cache = LRUCacheDoublyLinked(1)
        
        cache.put(1, 1)
        self.assertEqual(cache.get(1), 1)
        
        cache.put(2, 2)  # 1が削除される
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 2)
    
    def test_get_updates_order(self):
        """get操作が順序を更新するテスト"""
        cache = LRUCacheDoublyLinked(3)
        
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        
        # 1を取得すると、1が最も最近使われた要素になる
        cache.get(1)
        
        # 4を追加すると、2が削除される（1は最近使われたので残る）
        cache.put(4, 4)
        self.assertEqual(cache.get(1), 1)  # 1は残っている
        self.assertEqual(cache.get(2), -1)  # 2は削除された
        self.assertEqual(cache.get(3), 3)  # 3は残っている
        self.assertEqual(cache.get(4), 4)  # 4は残っている


def run_comparison_test():
    """両方の実装が同じ結果を返すことを確認"""
    print("\n" + "="*60)
    print("両実装の比較テスト")
    print("="*60 + "\n")
    
    test_cases = [
        {
            "name": "基本テスト",
            "capacity": 2,
            "operations": [
                ("put", (1, 1), None),
                ("put", (2, 2), None),
                ("get", (1,), 1),
                ("put", (3, 3), None),
                ("get", (2,), -1),
                ("put", (4, 4), None),
                ("get", (1,), -1),
                ("get", (3,), 3),
                ("get", (4,), 4),
            ]
        },
        {
            "name": "更新テスト",
            "capacity": 2,
            "operations": [
                ("put", (1, 1), None),
                ("put", (2, 2), None),
                ("put", (1, 10), None),
                ("get", (1,), 10),
                ("put", (3, 3), None),
                ("get", (2,), -1),
            ]
        },
    ]
    
    for test_case in test_cases:
        print(f"テスト: {test_case['name']}")
        cache1 = LRUCacheOrderedDict(test_case["capacity"])
        cache2 = LRUCacheDoublyLinked(test_case["capacity"])
        
        for op, args, expected in test_case["operations"]:
            if op == "put":
                result1 = cache1.put(args[0], args[1])
                result2 = cache2.put(args[0], args[1])
            elif op == "get":
                result1 = cache1.get(args[0])
                result2 = cache2.get(args[0])
                
                if result1 != result2:
                    print(f"  ❌ 不一致: {op}{args} -> OrderedDict: {result1}, DoublyLinked: {result2}")
                else:
                    print(f"  ✅ {op}{args} -> {result1}")
        
        print()


if __name__ == "__main__":
    print("="*60)
    print("LRU Cache テストスイート")
    print("="*60 + "\n")
    
    # unittestテストを実行
    print("1. OrderedDict版のテスト")
    unittest.main(argv=[''], exit=False, verbosity=2)
    
    # 比較テストを実行
    run_comparison_test()
    
    print("\n" + "="*60)
    print("すべてのテストが完了しました！")
    print("="*60)

