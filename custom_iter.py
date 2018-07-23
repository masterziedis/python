class Counter:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __iter__(self):
        return iter("hello")

    def __next__(self):
        if self.low < self.high:
            num = self.low
            self.low += 1
            return num
        return StopIteration
