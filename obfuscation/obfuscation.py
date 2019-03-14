import functools

def do(func):
    @functools.wraps(func)
    def OMG(*args, **kwargs):
        return func(*args, **kwargs)
    return OMG

class IDontKnowWhatIsThis():
    def __init__(self):
        self.a = []
        self.n = 0
        self.doSomething(self)

    @do
    def doSomething(self, *args, **kwargs):
        with open("input_file.txt", "r") as f:
            self.n = int(f.readline())
        self.doSomethingElse(self)

    @do
    def doSomethingElse(self, *args, **kwargs):
        a = []
        for i in range(self.n + 1):
            a.append(i)
        self.a = a[:]
        self.doSomethingAgain(self)

    @do
    def doSomethingAgain(self, *args, **kwargs):
        a = self.a
        a.insert(1, 0)
        self.a = a[:]
        self.doSomethingSpecial()

    @do
    def doSomethingSpecial(self, *args, **kwargs):
        a = self.a
        i = 2
        while i <= self.n:
            if a[i] != 0:
                j = i + i
                while j <= self.n:
                    a[j] = 0
                    j = j + i
            i += 1
        self.doSomethingMan()

    @do
    def doSomethingMan(self, *args, **kwargs):
        a = set(self.a)
        a.remove(0)
        print(a)


IDontKnowWhatIsThis()