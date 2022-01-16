from typing import List, Optional
from base.linked_list.ListNode import ListNode
import random


class Solution():
    def __init__(self, head: Optional[ListNode]) -> None:
        self.arr = []
        while head:
            self.arr.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.arr)


if __name__ == "__main__":
    pass