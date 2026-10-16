class Coffee:
    SIZES = ("Small", "Medium", "Large")

    def __init__(self, size, price):
        self._size = None  # set by the validated setter below
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        # Only accept Small, Medium or Large; otherwise warn and keep the old value
        if value in Coffee.SIZES:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1
