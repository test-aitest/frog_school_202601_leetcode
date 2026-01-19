"""
LRU Cache
Medium
Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

LRUCache(int capacity) Initialize the LRU cache of size capacity.
int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
A key is considered used if a get or a put operation is called on it.

Ensure that get and put each run in O(1) average time complexity.

Constraints:

1 <= capacity <= 100
0 <= key <= 1000
0 <= value <= 1000


https://neetcode.io/problems/lru-cache/question?list=neetcode150
"""

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.array = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.hashmap:
            return self.hashmap[key]
        return -1

    def put(self, key: int, value: int) -> None:
        """
        if len(array) == capacity, 
        we have to remove a old item and add a new item
        we append a new item into array
        """
        if len(self.array) == self.capacity:
            old_key = self.array[0]
            self.hashmap.pop(old_key)
            self.array = self.array[1:]
        self.array.append(key)
        self.hashmap[key] = value