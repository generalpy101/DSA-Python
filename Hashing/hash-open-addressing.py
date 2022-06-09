class MyHash:
    def __init__(self, size):
        self.size = 0
        self.max_size = size
        self._list = [-999 for i in range(size)]
        # -999 for empty and -9999 for deleted slot
        #None and a special node can be used in place of these
        #using numbers for ease

    def _hash_1(self, key):
        if not type(key) == type(1):
            raise TypeError("key must be integer")

        return key % self.max_size

    def _hash_2(self, key):
        if not type(key) == type(1):
            raise TypeError("key must be integer")

        return (self.max_size - 1) - key % (self.max_size - 1)

    def insert_linear_probing(self, key):
        if key is None:
            raise ValueError("key must not be None")
        if self.search_linear_probing(key):
            return False
        size = self.size
        if self.size == self.max_size:
            return False
        _hash = self._hash_1(key)
        i = _hash
        table = self._list
        while table[i] not in (-999, -9999):
            i = (i + 1) % self.max_size
        
        table[i] = key
        self.size += 1
        return True
        
    def remove_linear_probing(self,key) :
        if key is None :
            raise ValueError("Key must not be None")
        
        _hash = self._hash_1(key)
        i = _hash
        table = self._list
        while table[i] != -999:
            if table[i] == key:
                table[i] = -9999
                return True
            i = (i + 1) % self.max_size
            if i == _hash:
                return False

    def search_linear_probing(self, key):
        if key is None:
            raise ValueError("Key must not be None")

        _hash = self._hash_1(key)
        i = _hash
        table = self._list
        while table[i] != -999:
            if table[i] == key:
                return True
            i = (i + 1) % self.max_size
            if i == _hash:
                return False
        return False


if __name__ == "__main__":
    h = MyHash(7)
    print(f"Insert 1 : {h.insert_linear_probing(1)}")
    print(f"Insert 2 : {h.insert_linear_probing(2)}")
    print(f"Insert 3 : {h.insert_linear_probing(3)}")
    print(f"Search 3 : {h.search_linear_probing(3)}")
    print(f"Search 5 : {h.search_linear_probing(5)}")
    print(f"Search 1 : {h.search_linear_probing(1)}")
    print(f"Remove 2 : {h.remove_linear_probing(2)}")
    print(f"Search 2 : {h.search_linear_probing(2)}")
