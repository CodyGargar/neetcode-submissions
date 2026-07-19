class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.my_list = {}

    def get(self, key: int) -> int:
        if key in self.my_list:
            value = self.my_list.pop(key)
            self.my_list[key] = value
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.my_list:
            self.my_list.pop(key)
        self.my_list[key] = value
        if len(self.my_list) > self.capacity:
            self.my_list.pop(next(iter(self.my_list)))
