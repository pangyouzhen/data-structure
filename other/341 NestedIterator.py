class NestedInteger:

    def __init__(self, item):
        super().__init__()
        if type(item) == list:
            self.item = [NestedInteger(i) for i in item]
            self._is_int = False
        else:
            self.item = item
            self._is_int = True

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return self._is_int

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        if self.isInteger():
            return self.item

    def getList(self) -> "NestedInteger":
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        if not self.isInteger():
            return self.item


from collections.abc import Iterable


def flatten(items):
    for x in items:
        if isinstance(x, Iterable):
            yield from flatten(x)
        else:
            yield x


def flatten_list(items, res):
    for x in items:
        if isinstance(x, Iterable):
            flatten_list(x, res)
        else:
            res.append(x)


items = [1, 2, 3, [4, 5, [6]]]
# for i in flatten(items):
#     print(i)

res = []
flatten_list(items, res)
print(res)


class NestedIterator:
    def __init__(self, nestedList: "NestedInteger"):
        self.nestedList = nestedList
        self.g = self.gen()

    def gen(self):
        while self.nestedList:
            if self.nestedList[0].isInteger():
                nni = self.nestedList.pop(0)
                yield nni.getInteger()
            else:
                ni = NestedIterator(self.nestedList.pop(0).getList())
                for c in ni.g:
                    yield c

    def next(self) -> int:
        return self.ret

    def hasNext(self) -> bool:
        try:
            self.ret = next(self.g)
            return True
        except StopIteration:
            return False
