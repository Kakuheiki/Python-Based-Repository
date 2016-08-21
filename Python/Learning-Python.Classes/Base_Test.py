class First(object):
    def __init__(self):
        super(First, self).__init__()
        self.name = "Gilbert"

class Second(object):
    def __init__(self):
        super(Second, self).__init__()
        self.age = 15

class Third(First, Second):
    def __init__(self):
        super(Third, self).__init__()


Three = Third()


print Three.name
print Three.age
