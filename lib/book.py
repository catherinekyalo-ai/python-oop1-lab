class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None  # set by the validated setter below
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # Only accept integers; otherwise warn and keep the old value
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
