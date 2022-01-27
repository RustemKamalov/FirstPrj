class Buffer:
    def __init__(self):
        self._list = []

    def add(self, *a):
        for i in a:
            self._list.append(i)
            if len(self._list) == 5:
                print(sum(self._list))
                self._list.clear()

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
