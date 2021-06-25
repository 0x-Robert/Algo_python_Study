class SinEx:
    _sing =None

    def __new__(self, *args, **kwargs):
        if not self._sing:
            self._sing = super(SinEx, self).__new__(self, *args, **kwargs)
        return self._sing


x = SinEx()
print("x",x)

y = SinEx()
print("x == y check: ",x==y)
print("y",y)