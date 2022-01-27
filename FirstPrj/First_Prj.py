class MoneyBox:
    def __init__(self, capacity = 100):
        self.full_count = capacity
        self.count = 0

    def can_add(self, v):
        if self.count + v <= self.full_count:
            return True
        return False

    def add(self, v):
        if self.can_add(v):
            self.count += v

n = int(input())
money_box = MoneyBox(n)
money_box.add(12)
