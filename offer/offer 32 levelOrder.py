from base.tree.tree_node import TreeNode
from typing import List

class Solution:
    # offer32 II
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res,curr = [],[root]
        while curr:
            next_levels,curr_vals = [],[]
            for i in curr:
                if i.left:
                    next_levels.append(i.left)
                if i.right:
                    next_levels.append(i.right)
                curr_vals.append(i.val)
            curr = next_levels
            res.append(curr_vals)
        return res
        
                
    # offer 32 I
    def level2(self,root:TreeNode) -> List[int]:
        if not root:
            return []
        res, curr = [],[root]
        while curr:
            node = curr.pop(0)
            if node.left:
                curr.append(node.left)
            if node.right:
                curr.append(node.right)
            res.append(node.val)
        return res
    
    # offer 32 III
    def level3(self,root:TreeNode) -> List[List[int]]:
        if not root:
            return []
        res,curr,n = [],[root],0
        while curr:
            next_levels, curr_vals = [],[]
            for i in curr:
                if i.left:
                    next_levels.append(i.left)
                if i.right:
                    next_levels.append(i.right)
                curr_vals.append(i.val)
            if n % 2 == 0:
                res.append(curr_vals)
            else:
                res.append(curr_vals[::-1])
            curr = next_levels
            n+=1
        return res
            
    

if __name__ == '__main__':
    tree = TreeNode.from_strs("[3, 9, 20, null, null, 15, 7]")
    print(tree)
    sol = Solution()
    # t = sol.levelOrder(tree)
    # t = sol.level2(tree)
    t = sol.level3(tree)
    print(t)
