class OrderedStream:

    def __init__(self, n: int):
        self.store = [""] * n
        self.ptr = 0
    def insert(self, idKey: int, value: str) -> List[str]:
        self.store[idKey - 1] = value
        copy = []
        if idKey -1  == self.ptr:
            for  i in range(self.ptr, len(self.store)):
                if self.store[i] == "":
                    break
                copy.append(self.store[i])

        self.ptr += len(copy)
        return copy

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)