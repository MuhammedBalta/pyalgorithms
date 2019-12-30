class QuickUnionUF:
    def __init__(self, N):
        self.id = []
        for i in range(N):
            self.id.insert(i, i)

    def root(self, index):
        if index == self.id[index]:
            return index
        else:
            return self.root(self.id[index])

    def isConnected(self, p, q):
        if self.root(p) == self.root(q):
            return True
        else:
            return False

    def union(self, p, q):
        if self.isConnected(p,q) == False:
            proot = self.root(p)
            qroot = self.root(q)
            self.id[proot] = qroot


