class Jar:

    def __init__(self, capacity=12):
        if not capacity > 0:
            raise ValueError("Invalid Number of Cookies")
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * '🍪'

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Deposit Error")
        self.size = self.size + n

    def withdraw (self, n):
        if self.size - n < 0:
            raise ValueError("Withdraw Error")
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise valueError('capacity error')
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise valueError('Size error')
        self._size = size

def main():
    jar = Jar()
    #print(jar)
    jar.deposit(13)
    print(jar)


if __name__ == "__main__":
    main()
