class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return pos >= neg

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return pos >= 1

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.iterable = []
        for i in iterable:
            self.pos = 0
            self.neg = 0
            for f in funcs:
                if f(i):
                    self.pos += 1
                else:
                    self.neg += 1
            if judge(self.pos, self.neg):
                self.iterable.append(i)

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        return iter(self.iterable)


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]
print(list(multifilter(a, mul2, mul3, mul5)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
