class MyHash:
    def __init__(self, b):
        self.Bucket = b
        self.table = [[] for x in range(b)]

    def insert(self, x):
        i = x%self.Bucket
        self.table[i].append(x)

    def remove(self, x):
        i = x%self.Bucket
        if x in self.table[i]:
            self.table[i].remove(x)

    def search(self, x):
        i = x% self.Bucket
        return x in self.table[i]
    

chain = MyHash(5)
chain.insert(70)
chain.insert(71)
chain.insert(9)
chain.insert(56)
chain.insert(72)

print(chain.search(56))

chain.remove(71)

print(chain.search(71))