from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_val = {}  # Stores {key: value}
        self.key_to_freq = {}  # Stores {key: frequency}
        self.freq_to_keys = defaultdict(OrderedDict)  # Maps frequency to OrderedDict of keys
        self.min_freq = 0  # Tracks the minimum frequency

    def _update_freq(self, key):
        """Helper function to update the frequency of a key"""
        freq = self.key_to_freq[key]
        val = self.key_to_val[key]

        # Remove key from the current frequency list
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:  # Clean up empty frequency lists
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1  # Increment min_freq only if it was the removed one

        # Move key to the next frequency list
        new_freq = freq + 1
        self.key_to_freq[key] = new_freq
        self.freq_to_keys[new_freq][key] = val

    def get(self, key: int) -> int:
        """Retrieve a value from cache and update its frequency"""
        if key not in self.key_to_val:
            return -1
        self._update_freq(key)
        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        """Insert a new key-value pair or update existing key"""
        if self.capacity == 0:
            return

        if key in self.key_to_val:
            # Update value
            self.key_to_val[key] = value
            self._update_freq(key)
        else:
            if len(self.key_to_val) >= self.capacity:
                # Remove the least frequently used key
                lfu_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
                del self.key_to_val[lfu_key]
                del self.key_to_freq[lfu_key]
                
                # Clean up empty frequency list
                if not self.freq_to_keys[self.min_freq]:
                    del self.freq_to_keys[self.min_freq]

            # Insert new key-value pair
            self.key_to_val[key] = value
            self.key_to_freq[key] = 1
            self.freq_to_keys[1][key] = value
            self.min_freq = 1  # Reset min frequency to 1

# Example Usage
lfu = LFUCache(2)
lfu.put(1, 10)  # Cache: {1:10}
lfu.put(2, 20)  # Cache: {1:10, 2:20}
print(lfu.get(1))  # Returns 10, updates frequency of 1
lfu.put(3, 30)  # Removes key 2 (LFU), adds key 3: Cache {1:10, 3:30}
print(lfu.get(2))  # Returns -1 (not found)
print(lfu.get(3))  # Returns 30
