# Write a Python class to implement an LRU (Least Recently Used) Cache. The class should support two operations: get(key) and put(key, value). The cache should have a fixed capacity.
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity  # Maximum number of items the cache can hold
        self.cache = OrderedDict()  # Store cache items in an ordered dictionary
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1  # Return -1 if the key is not found
        else:
            # Move the accessed item to the end to mark it as recently used
            self.cache.move_to_end(key)
            return self.cache[key]
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If key already exists, update the value and move to end
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            # If the cache is full, remove the least recently used (first) item
            self.cache.popitem(last=False)
        # Insert the item (or update it if already present)
        self.cache[key] = value
# Example Usage:
lru_cache = LRUCache(2)
lru_cache.put(1, 1)  # Cache is {1=1}
lru_cache.put(2, 2)  # Cache is {1=1, 2=2}
print(lru_cache.get(1))  # Returns 1, Cache is {2=2, 1=1}
lru_cache.put(3, 3)  # Evicts key 2, Cache is {1=1, 3=3}
print(lru_cache.get(2))  # Returns -1 (not found)
lru_cache.put(4, 4)  # Evicts key 1, Cache is {3=3, 4=4}
print(lru_cache.get(1))  # Returns -1 (not found)
print(lru_cache.get(3))  # Returns 3
print(lru_cache.get(4))  # Returns 4