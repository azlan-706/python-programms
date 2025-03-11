class MRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # Dictionary to store key-value pairs
        self.stack = []  # Stack to track MRU order

    def get(self, key):
        """Retrieve a value and update MRU order"""
        if key in self.cache:
            self.stack.remove(key)  # Move key to most recent position
            self.stack.append(key)
            return self.cache[key]
        return -1  # Key not found

    def put(self, key, value):
        """Insert a key-value pair or update existing key"""
        if key in self.cache:
            self.stack.remove(key)  # Remove old position

        elif len(self.cache) >= self.capacity:
            most_recently_used_key = self.stack.pop()  # Evict MRU key
            del self.cache[most_recently_used_key]

        self.cache[key] = value
        self.stack.append(key)  # Mark as most recently used

# Usage
mru_cache = MRUCache(3)
mru_cache.put(1, 'A')
mru_cache.put(2, 'B')
mru_cache.put(3, 'C')
print(mru_cache.get(3))  # Output: 'C'
mru_cache.put(4, 'D')    # Evicts key 3
print(mru_cache.get(3))  # Output: -1 (corrected)
print(mru_cache.get(1))  # Output: 'A'
