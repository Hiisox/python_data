class calculator:
    def __init__(self, object):
        self.object = object
    def __add__(self, object) -> None:
        self.object = [self.object[x] + object for x in range(len(self.object))]
        print(self.object)
    def __mul__(self, object) -> None:
        self.object = [self.object[x] * object for x in range(len(self.object))]
        print(self.object)
    def __sub__(self, object) -> None:
        self.object = [self.object[x] - object for x in range(len(self.object))]
        print(self.object)
    def __truediv__(self, object) -> None:
        if object == 0:
            print("division by 0 is not possible")
            return
        self.object = [self.object[x] / object for x in range(len(self.object))]
        print(self.object)