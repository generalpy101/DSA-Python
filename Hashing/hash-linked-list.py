class MyHash :
    def __init__(self,bucket = 7) :
        self.bucket = bucket
        self._list = [[] for i in range(bucket)]

    def insert(self,key) :
        if key is None :
            raise ValueError("Key must not be None")
        hashForKey = self._hash(key)
        if self.search(key) is True :
            self.remove(key,True)
        self._list[hashForKey].append(key)
        print(f"Key {key} inserted successfully")
        
    def remove(self,key,internal=False) :
        hashForKey = self._hash(key)
        if internal :
            self._list[hashForKey].remove(key)
            return
        if key is None :
            raise ValueError("Key must not be None")
        if self.search(key) is False :
            raise KeyError(f"Key {key} not found")
        self._list[hashForKey].remove(key)
        print(f"Key {key} removed successfully")
                
    def search(self,key) :
        if key is None :
            raise ValueError("Key must not be None")
        hashForKey = self._hash(key)
        if len(self._list[hashForKey]) == 0 :
            return False
        else :
            if len(self._list[hashForKey]) == 1:
                return True if self._list[hashForKey][0] == key else False
            else :
                for i in self._list[hashForKey] :
                    if i == key :
                        return True
                return False
    
    def _hash(self,key) :
        #creating simple hash function 
        if type(key) != type(1) :
            raise ValueError("Key must be integer for this simple hash function")
        return key % self.bucket
    
if __name__ == "__main__" :
    hashing = MyHash(7)
    hashing.insert(10)
    hashing.insert(70)
    hashing.insert(1)
    hashing.insert(22)
    hashing.insert(22)
    print(hashing.search(10))
    print(hashing.search(245))
    print(hashing.search(70))
    print(hashing.search(22))
    hashing.remove(22)
    print(hashing.search(22))