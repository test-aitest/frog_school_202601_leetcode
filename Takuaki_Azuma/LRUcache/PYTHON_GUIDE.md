# Python書き方ガイド - LRU Cache実装を通じて学ぶ

このドキュメントでは、LRU Cacheの実装を通じてPythonの重要な書き方を学びます。

## 目次

1. [クラスの定義](#クラスの定義)
2. [型ヒント](#型ヒント)
3. [特殊メソッド](#特殊メソッド)
4. [データ構造の使い方](#データ構造の使い方)
5. [アルゴリズムの実装パターン](#アルゴリズムの実装パターン)

---

## クラスの定義

### 基本的なクラス定義

```python
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
```

**ポイント:**
- `class`キーワードでクラスを定義
- `__init__`はコンストラクタ（初期化メソッド）
- `self`はインスタンス自身を指す（必須の第一引数）
- `self.capacity`のように`self.`を付けてインスタンス変数を定義

### メソッドの定義

```python
def get(self, key: int) -> int:
    """メソッドの説明"""
    if key not in self.cache:
        return -1
    return self.cache[key]
```

**ポイント:**
- メソッドの第一引数は必ず`self`
- 型ヒントで引数と戻り値の型を指定できる
- ドキュメント文字列（docstring）で説明を書く

---

## 型ヒント

Python 3.5以降では型ヒントが使えます。コードの可読性とIDEの補完が向上します。

### 基本的な型ヒント

```python
def get(self, key: int) -> int:
    # keyはint型、戻り値もint型
    pass

def put(self, key: int, value: int) -> None:
    # 戻り値がない場合はNoneを指定
    pass
```

### 複合型の型ヒント

```python
from typing import Dict, Optional, List

def process_data(self, data: Dict[str, int]) -> Optional[List[int]]:
    # Dict[str, int]: 文字列キー、整数値の辞書
    # Optional[List[int]]: 整数のリストまたはNone
    pass
```

---

## 特殊メソッド

### `__init__` - コンストラクタ

```python
def __init__(self, capacity: int):
    """インスタンス作成時に自動的に呼ばれる"""
    self.capacity = capacity
```

### `__str__` / `__repr__` - 文字列表現

```python
def __str__(self) -> str:
    """print()で表示される文字列"""
    return f"LRUCache(capacity={self.capacity})"

def __repr__(self) -> str:
    """開発者向けの詳細な文字列表現"""
    return f"LRUCache(capacity={self.capacity}, size={len(self.cache)})"
```

---

## データ構造の使い方

### 1. 辞書（dict）

```python
# 辞書の作成
cache = {}

# 値の追加・更新
cache[key] = value

# 値の取得
value = cache[key]  # キーが存在しない場合はKeyError
value = cache.get(key, default)  # キーが存在しない場合はdefaultを返す

# キーの存在確認
if key in cache:
    # 処理

# キーの削除
del cache[key]
value = cache.pop(key, default)  # 削除して値を返す

# サイズの取得
size = len(cache)
```

### 2. OrderedDict

```python
from collections import OrderedDict

# OrderedDictの作成
cache = OrderedDict()

# 値の追加
cache[key] = value

# 最後に移動（最近使用したことを示す）
cache.move_to_end(key)

# 先頭の要素を削除
oldest_key, oldest_value = cache.popitem(last=False)

# 末尾の要素を削除
newest_key, newest_value = cache.popitem(last=True)  # デフォルト
```

**OrderedDictの特徴:**
- 挿入順序を保持する辞書
- `move_to_end()`でO(1)で要素を移動可能
- LRU Cacheの実装に最適

### 3. 連結リスト（カスタム実装）

```python
class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None  # 前のノード
        self.next = None  # 次のノード
```

**ポイント:**
- 双方向連結リストでは各ノードが前後の参照を持つ
- ノードの追加・削除がO(1)で可能
- メモリ効率が良い

---

## アルゴリズムの実装パターン

### パターン1: 存在確認 → 処理

```python
def get(self, key: int) -> int:
    if key not in self.cache:
        return -1  # 存在しない場合の処理
    
    # 存在する場合の処理
    self.cache.move_to_end(key)
    return self.cache[key]
```

### パターン2: 存在確認 → 分岐処理

```python
def put(self, key: int, value: int) -> None:
    if key in self.cache:
        # 既存のキーの更新
        self.cache[key] = value
        self.cache.move_to_end(key)
    else:
        # 新しいキーの追加
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

### パターン3: ヘルパーメソッドの活用

```python
def _add_node(self, node: Node) -> None:
    """プライベートメソッド（_で始まる）"""
    # 内部で使用するヘルパーメソッド
    pass

def _remove_node(self, node: Node) -> None:
    """プライベートメソッド"""
    pass
```

**ポイント:**
- `_`で始まるメソッドは「プライベート」の慣習
- コードの再利用性と可読性が向上
- 複雑な処理を小さな関数に分割

---

## Pythonのベストプラクティス

### 1. コメントとドキュメント

```python
def get(self, key: int) -> int:
    """
    キーに対応する値を取得
    
    Args:
        key: 取得したいキー
    
    Returns:
        キーが存在する場合: 対応する値
        キーが存在しない場合: -1
    
    時間計算量: O(1)
    """
    pass
```

### 2. アサーション（デバッグ用）

```python
def put(self, key: int, value: int) -> None:
    assert self.capacity > 0, "capacity must be positive"
    # 処理
```

### 3. エラーハンドリング

```python
def get(self, key: int) -> int:
    try:
        return self.cache[key]
    except KeyError:
        return -1
```

### 4. 条件式の簡潔な書き方

```python
# 良い例
return self.cache[key] if key in self.cache else -1

# より明示的な例（推奨）
if key not in self.cache:
    return -1
return self.cache[key]
```

---

## 実装の比較

### OrderedDict版（シンプル）

**メリット:**
- コードが短く、理解しやすい
- Pythonの標準ライブラリを活用
- 実装が簡単

**デメリット:**
- OrderedDictの内部実装に依存
- アルゴリズムの理解が浅くなる可能性

### 双方向連結リスト版（教育的）

**メリット:**
- アルゴリズムの理解が深まる
- 基本的なデータ構造の組み合わせを学べる
- 他の言語にも応用可能

**デメリット:**
- コードが長くなる
- 実装が複雑

---

## 学習の進め方

1. **OrderedDict版を理解する**
   - コードを読んで、動作を追う
   - 実際に実行して動作を確認

2. **双方向連結リスト版を理解する**
   - 各メソッドの役割を理解
   - ノードの追加・削除の流れを追う

3. **自分で実装してみる**
   - コメントを見ずに実装
   - テストケースで動作確認

4. **最適化を考える**
   - 時間計算量・空間計算量を確認
   - エッジケースを考える

---

## 参考リソース

- [Python公式ドキュメント](https://docs.python.org/ja/3/)
- [collections.OrderedDict](https://docs.python.org/ja/3/library/collections.html#collections.OrderedDict)
- [型ヒント（PEP 484）](https://peps.python.org/pep-0484/)

