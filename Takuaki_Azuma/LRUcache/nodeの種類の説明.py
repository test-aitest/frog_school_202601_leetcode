"""
Nodeの種類と用途 / Types and Uses of Node

Nodeは用途によって異なる構造を持ちます。
Node has different structures depending on its use.
"""

# ============================================
# 1. 単方向連結リストのNode
# ============================================

class SinglyLinkedListNode:
    """
    単方向連結リスト（Singly Linked List）のNode
    
    前方向のみの参照を持ちます。
    Has reference only to the next node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None  # 次のノードのみ


# ============================================
# 2. 双方向連結リストのNode（今回のLRU Cache）
# ============================================

class DoublyLinkedListNode:
    """
    双方向連結リスト（Doubly Linked List）のNode
    
    前後2方向の参照を持ちます。
    Has references to both previous and next nodes.
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None  # 前のノード
        self.next = None  # 次のノード


# ============================================
# 3. 2Dグリッド（上下左右4方向）のNode
# ============================================

class GridNode:
    """
    2Dグリッド（Grid）のNode
    
    上下左右4方向の参照を持ちます。
    Has references to up, down, left, right.
    
    用途: 迷路探索、画像処理、ゲームのマップなど
    Uses: Maze solving, image processing, game maps, etc.
    """
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.up = None      # 上のノード
        self.down = None    # 下のノード
        self.left = None    # 左のノード
        self.right = None   # 右のノード


# ============================================
# 4. 木構造（Tree）のNode
# ============================================

class TreeNode:
    """
    二分木（Binary Tree）のNode
    
    親と2つの子への参照を持ちます。
    Has reference to parent and two children.
    
    用途: データベースのインデックス、ヒープ、式の解析など
    Uses: Database indexes, heaps, expression parsing, etc.
    """
    def __init__(self, val):
        self.val = val
        self.left = None   # 左の子ノード
        self.right = None  # 右の子ノード
        self.parent = None  # 親ノード（オプション）


# ============================================
# 5. グラフ（Graph）のNode
# ============================================

class GraphNode:
    """
    グラフ（Graph）のNode
    
    複数の隣接ノードへの参照を持ちます。
    Has references to multiple adjacent nodes.
    
    用途: ソーシャルネットワーク、経路探索、依存関係など
    Uses: Social networks, path finding, dependencies, etc.
    """
    def __init__(self, val):
        self.val = val
        self.neighbors = []  # 隣接ノードのリスト（複数）


# ============================================
# 実際の使用例
# ============================================

print("=" * 60)
print("Nodeの種類と用途 / Types and Uses of Node")
print("=" * 60)

print("\n1. 単方向連結リスト（Singly Linked List）")
print("   [Node1] -> [Node2] -> [Node3]")
print("   用途: スタック、キュー、シンプルなリスト")
print("   Uses: Stack, Queue, Simple list")

print("\n2. 双方向連結リスト（Doubly Linked List）← 今回のLRU Cache")
print("   [Node1] <-> [Node2] <-> [Node3]")
print("   用途: LRU Cache、ブラウザの履歴、Undo/Redo機能")
print("   Uses: LRU Cache, Browser history, Undo/Redo")

print("\n3. 2Dグリッド（Grid）4方向")
print("        [上]")
print("          ↑")
print("   [左] [Node] [右]")
print("          ↓")
print("        [下]")
print("   用途: 迷路探索、画像処理、ゲームのマップ")
print("   Uses: Maze solving, Image processing, Game maps")

print("\n4. 木構造（Tree）")
print("        [Node]")
print("        /    \\")
print("   [左子]  [右子]")
print("   用途: データベース、ヒープ、式の解析")
print("   Uses: Database, Heap, Expression parsing")

print("\n5. グラフ（Graph）")
print("   [Node1] -- [Node2]")
print("     |          |")
print("   [Node3] -- [Node4]")
print("   用途: ソーシャルネットワーク、経路探索")
print("   Uses: Social networks, Path finding")

# ============================================
# 4方向Nodeの実装例（迷路探索）
# ============================================

print("\n" + "=" * 60)
print("4方向Nodeの実装例: 迷路探索 / 4-direction Node Example: Maze")
print("=" * 60)

class MazeNode:
    """迷路の各セルを表すNode"""
    def __init__(self, row, col, is_wall=False):
        self.row = row
        self.col = col
        self.is_wall = is_wall
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.visited = False  # 探索済みかどうか

# 3x3の迷路を作成
maze = []
for i in range(3):
    row = []
    for j in range(3):
        node = MazeNode(i, j, is_wall=(i == 1 and j == 1))
        row.append(node)
    maze.append(row)

# 4方向を連結
for i in range(3):
    for j in range(3):
        node = maze[i][j]
        if i > 0:
            node.up = maze[i-1][j]
        if i < 2:
            node.down = maze[i+1][j]
        if j > 0:
            node.left = maze[i][j-1]
        if j < 2:
            node.right = maze[i][j+1]

print("\n3x3の迷路を作成しました:")
for i in range(3):
    for j in range(3):
        node = maze[i][j]
        neighbors = []
        if node.up: neighbors.append("上")
        if node.down: neighbors.append("下")
        if node.left: neighbors.append("左")
        if node.right: neighbors.append("右")
        print(f"  [{i},{j}]: 接続方向 = {neighbors}")

print("\n" + "=" * 60)
print("【まとめ】")
print("=" * 60)
print("✅ Nodeの構造は用途によって異なる")
print("✅ 単方向: nextのみ")
print("✅ 双方向: prev, next（今回のLRU Cache）")
print("✅ 4方向: up, down, left, right（グリッド）")
print("✅ 木構造: left, right, parent")
print("✅ グラフ: neighbors（複数）")
print("\n")
print("✅ Node structure differs by use case")
print("✅ Singly: next only")
print("✅ Doubly: prev, next (this LRU Cache)")
print("✅ 4-direction: up, down, left, right (grid)")
print("✅ Tree: left, right, parent")
print("✅ Graph: neighbors (multiple)")


