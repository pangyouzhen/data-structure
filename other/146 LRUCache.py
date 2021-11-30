from collections import deque


class LRUCache:
    #  不能使用 字典放在deque里面，因为超时
    def __init__(self, capacity: int):
        self.keys_deque = deque(maxlen=capacity)
        self.value_deque = deque(maxlen=capacity)

    def get(self, key: int) -> int:
        if key in self.keys_deque:
            key_index = self.keys_deque.index(key)
            value = self.value_deque[key_index]
            del self.keys_deque[key_index]
            del self.value_deque[key_index]
            self.keys_deque.appendleft(key)
            self.value_deque.appendleft(value)
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys_deque:
            key_index = self.keys_deque.index(key)
            del self.keys_deque[key_index]
            del self.value_deque[key_index]
        self.keys_deque.appendleft(key)
        self.value_deque.appendleft(value)


# Your LRUCache object will be instantiated and called as such:
if __name__ == '__main__':
    cache = LRUCache(2)
    assert cache.get(2) == -1
    cache.put(2, 6)
    # cache.put(1, 1)
    assert cache.get(1) == -1
    # cache.put(3, 3)
    # assert cache.get(2) == -1
    # cache.put(4, 4)
    # assert cache.get(1) == -1
    # assert cache.get(3) == 3
    # assert cache.get(4) == 4
    # obj.put(key,value)
    cache.put(1, 5)
    cache.put(1, 2)
    print(cache.get(1))
    print(cache.get(2))
