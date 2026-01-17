# `__init__`メソッドの理解

## あなたの理解について

「使うパーツを定義する関数」という理解は**ほぼ正しい**ですが、より正確には：

**`__init__`は「オブジェクトの初期状態を設定するメソッド（コンストラクタ）」です。**

## 詳しい説明

### 1. `__init__`の役割

```python
class LRUCache:
    def __init__(self, capacity: int):
        # ここで「初期状態」を設定します
        self.capacity = capacity      # 容量を保存
        self.cache = {}                # 空の辞書を作成
        self.head, self.tail = ...     # ダミーノードを作成
```

**重要なポイント:**
- オブジェクトが作成される**瞬間**に自動的に呼ばれる
- オブジェクトの**初期状態**を設定する
- 「使うパーツ」を準備する、という理解でOK！

### 2. いつ呼ばれるか？

```python
# この行でオブジェクトが作成されるとき、__init__が自動的に呼ばれる
cache = LRUCache(2)  # ← ここで __init__(self, 2) が実行される
```

### 3. 具体例で理解する

```python
class LRUCache:
    def __init__(self, capacity: int):
        # 「使うパーツ」を準備している
        self.capacity = capacity    # パーツ1: 容量
        self.cache = {}             # パーツ2: 辞書
        self.head = Node(0, 0)      # パーツ3: headノード
        self.tail = Node(0, 0)      # パーツ4: tailノード
        
        # パーツ同士を接続する
        self.head.next = self.tail
        self.tail.prev = self.head
```

**あなたの理解「使うパーツを定義する」は正しいです！**

より正確に言うと：
- **パーツを準備する**（変数を初期化する）
- **パーツを組み立てる**（初期状態を設定する）
- **使える状態にする**（オブジェクトを初期化する）

### 4. `__init__`と他のメソッドの違い

```python
class LRUCache:
    def __init__(self, capacity: int):
        # オブジェクト作成時に1回だけ呼ばれる
        # 初期状態を設定
        self.capacity = capacity
    
    def get(self, key: int) -> int:
        # オブジェクト作成後、何度でも呼べる
        # オブジェクトの状態を使って処理を行う
        return self.cache.get(key, -1)
    
    def put(self, key: int, value: int) -> None:
        # オブジェクト作成後、何度でも呼べる
        # オブジェクトの状態を変更する
        self.cache[key] = value
```

### 5. 実際の動作を見てみる

```python
# ステップ1: オブジェクトを作成
cache = LRUCache(2)
# → この瞬間、__init__が実行される
# → self.capacity = 2
# → self.cache = {}
# → self.head, self.tail が作成される

# ステップ2: メソッドを呼ぶ
cache.put(1, 1)
# → __init__は呼ばれない（既に初期化済み）
# → putメソッドが実行される

cache.get(1)
# → __init__は呼ばれない
# → getメソッドが実行される
```

## まとめ

| 項目 | 説明 |
|------|------|
| **役割** | オブジェクトの初期状態を設定する |
| **呼ばれるタイミング** | オブジェクト作成時（1回だけ） |
| **あなたの理解** | ✅ 「使うパーツを定義する」→ 正しい！ |
| **より正確な表現** | 「初期状態を設定する」「パーツを準備して組み立てる」 |

## 例: 家を建てることに例えると

```python
class House:
    def __init__(self, rooms: int):
        # 家を建てる時に必要なパーツを準備
        self.rooms = rooms        # 部屋数
        self.furniture = []       # 家具リスト（空）
        self.doors = []           # ドアリスト（空）
        # 家の初期状態が完成！

# 家を作る（__init__が実行される）
my_house = House(3)  # 3部屋の家が完成

# 家を使う（他のメソッド）
my_house.add_furniture("テーブル")  # 家具を追加
my_house.open_door(1)              # ドアを開ける
```

**`__init__` = 家を建てる時に必要なパーツを準備して、使える状態にする**

あなたの理解で問題ありません！👍

