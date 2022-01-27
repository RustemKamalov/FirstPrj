class Buffer:
    def __init__(self):
        self._list = []
        self._sum = 0

    def add(self, *a):
        count = len(self._list)
        for i in a:
            if count < 5:
                self._list.append(i)
                count += 1
                self._sum += i
                if count == 5:
                    print(self._sum)
                    count = 0
                    self._list = []
                    self._sum = 0

    def get_current_part(self):
        return self._list


buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part())
buf.add(4, 5, 6)
print(buf.get_current_part())
buf.add(7, 8, 9, 10)
print(buf.get_current_part())
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
print(buf.get_current_part())
