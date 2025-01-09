class Alphabet(list[chr]):
    def __init__(self, iterable=(), empty_char='#'):
        super().__init__(iterable)
        self._empty_char = empty_char
        self.append(self._empty_char)

    def __setitem__(self, index: int, value: chr):
        if not self.__contains__(value):
            super().__setitem__(int(index), chr(value))

    def __contains__(self, item: chr):
        if super().__contains__(item):
            return True
        # else:
        #     return item == self._empty_char

    def append(self, value: chr):
        if not self.__contains__(value):
            super().append(value)

    def insert(self, index: int, value: chr):
        if not self.__contains__(value):
            super().insert(index, value)

    def extend(self, iterable):
        for item in iterable:
            if not self.__contains__(item):
                super().append(item)

    @property
    def empty_char(self) -> chr:
        return self._empty_char


if __name__ == "__main__":
    a = Alphabet(["a", "b", "c", "x"])
    print(a)
    b = Alphabet(["a", "d"])
    print(b)
    print(f"Appending 'a' to alphabet")
    a.append("a")
    print(f"After append: {a}")
    a.extend(b)
    print(f"Appending {b} to alphabet")
    print(f"After append: {a}")
    print(f"Appending '#' to alphabet")
    a.append("#")
    print(f"After append: {a}")
