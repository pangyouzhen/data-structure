-------
贵有恒,何必三更眠五更起

最无益,莫过一日曝十日寒

-------

## 数据结构

### 图的两种表示方法

1. 邻接表
2. 邻接矩阵

### 回溯算法

回溯算法在树中就是dfs
```
backtracking() { 
    if (终止条件) {
         存放结果;
     }
     for (选择：选择列表（可以想成树中节点孩子的数量）) {
        递归，处理节点;
         backtracking(); 
        回溯，撤销处理结果 
    } }
```

递归
```
终止条件
递归过程
```
## 算法

1. 快速排序和merge排序一定要相当熟悉
1. 


### 常见的动态规划的转移方程

1. 最长公共子串
	1. `dp[0][j] = 0;  (0<=j<=m)`
	2. `dp[i][0] = 0;  (0<=i<=m)`
	3. `dp[i][j] = dp[i-1][j-1] + 1; (str1[i] == str2[j])`
	4. `dp[i][j] = 0; (str[i] != str[j])`
1. 最长公共子序列
	1. `dp[0][j] = 0; (0<=j<=m)`
	2. `dp[i][0] = 0;(0<=i<=m)`
	3. `dp[i][j] = dp[i-1][j-1] + 1; (str1[i] == str2[j])`
	4. `dp[i][j] = max(dp[i][j-1],dp[i-1][j]); (str1[i-1]!=str2[j-1])`
1. 最长递增子序列
   1. `F[x] = max(1,F[i] +1 | ai <ax && i<x)`
1. 最大子序列和
   1. `dp[1] = a1; (a1>0 && i==1)`
   1. `dp[1] = dp[i-1] +ai;(ai>=0 && i>=2)`
   1. `dp[i]=0; (dp[i-1] + a1 <= 0 && i>=2)`
1. 数塔问题
   1. `dp[i][j] = max(dp[i-1][j-1],dp[i-1][j] + data[i][j])`
1. 01背包问题
   1. `dp[i][j] = max(dp[i-1][j-v[i]]+c[i],dp[i-1][j])`
1. 矩阵连乘
   1. `dp[i][j]=0; i==j`
   1. `dp[i][j] = min(dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j]); (i<j && i<=k<j)`
   1. `dp[1][n] 为最终解`

### 其他
1. 很多算法能先排序就先排序
1. 输入规模和时间复杂度关系


### python-leetcode常用库和函数

1. `functools 中的 reduce函数`
2. `collections 中的 Counter`
3. `itertools 中的 permutations combinations`
4. `heapq`
5. `bisect`

### 典型问题


