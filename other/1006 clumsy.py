

class Solution:
    def clumsy(self, N):
        op = 0
        stack = [N]
        for i in range(N - 1, 0, -1):
            if op == 0:
                stack.append(stack.pop() * i)
            elif op == 1:
                stack.append(int(stack.pop() / float(i)))
            elif op == 2:
                stack.append(i)
            elif op == 3:
                stack.append(-i)
            op = (op + 1) % 4
        return sum(stack)



if __name__ == '__main__':
    a = Solution()
    print(a.clumsy(10))
