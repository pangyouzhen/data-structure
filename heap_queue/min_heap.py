class MinHeap:

    def __init__(self) -> None:
        self.array = []

    def __len__(self):
        return len(self.array)

    def extract_min(self):
        if not self.array:
            return None
        if len(self.array) == 1:
            return self.array.pop(0)

        minium = self.array[0]
        self.array[0] = self.array.pop(-1)
        self._buble_down(index=0)
        return minium

    def peek_min(self):
        return self.array[0] if self.array else None
    
    def insert(self,key):
        if key is None:
            raise TypeError('key cannot be None')
        self.array.append(key)
        self._buble_up(index=len(self.array)-1)

    def _buble_up(self,index):
        if index == 0:
            return 
        index_parent = (index - 1) // 2
        if self.array[index] < self.array[index_parent]:
            self.array[index],self.array[index_parent] = \
                self.array[index_parent],self.array[index]
            self._buble_up(index_parent)
        
    def _buble_down(self,index):
        min_child_index = self.find_smaller_child(index)
        if min_child_index == -1:
            pass
