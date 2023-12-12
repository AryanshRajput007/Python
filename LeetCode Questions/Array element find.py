#import array as arr

#array = arr.array('i', [1, 5, 2])
array = [1, 2, 5, 2, 2, 2]
array.insert(0, 2)
target = 2
print(array.index(target))
"""
low = 0
high = len(array) - 1

while low <= high:
    if array[low] < target:
        low += 1
    elif array[high] > target:
        high -= 1
    else:
        print(low)
        break
        """
"""
class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size

    def _get_hash(self, key):
        return hash(key) % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = [key_value]
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    break
            else:
                self.map[key_hash].append(key_value)

    def get(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]

        return None

    def remove(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is not None:
            for i, pair in enumerate(self.map[key_hash]):
                if pair[0] == key:
                    self.map[key_hash].pop(i)
                    break

"""
