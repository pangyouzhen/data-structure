class A:
    def a(self, t):
        global init_a
        init_a = []
        self.a_(t)
        return init_a

    def a_(self, t):
        init_a.append(t)


class B:
    def b(self, t):
        global init_b
        init_b = 0
        self.b_(t)
        return init_b
    #  为什么这个不起作用
    def b_(self, t):
        init_b += 1

if __name__ == '__main__':
    a_ins = A()
    b_ins = B()
    print(a_ins.a(5))
    print(b_ins.b(5))