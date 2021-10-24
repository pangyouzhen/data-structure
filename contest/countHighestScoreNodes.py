from typing import List


class Solution:
    # todo 图的深度优先遍历
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        """
        parents[i] 是节点 i 的父节点，翻译过来就是val是ind的父节点
        """
