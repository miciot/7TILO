from tm_common import *


class OutOfRangeError(Exception):
    def __init__(self, position: int):
        if position < 0:
            message = "Start of tape already reached, can't move again to left"
        else:
            message = "End of tape already reached, can't move again to right"
        super().__init__(message)


class Tape(list):
    # _position: int
    # _input: bool
    # _output: bool

    def __init__(self, iterable=(), _input=False, _output=False):
        super().__init__(iterable)
        self._position = 0
        self._input = _input
        self._output = _output

    def __setitem__(self, key: int, value: chr):
        super().__setitem__(key, value)

    @property
    def input(self) -> bool:
        return self._input

    @property
    def output(self) -> bool:
        return self._output

    @property
    def value(self) -> chr:
        return self.__getitem__(self._position)

    @value.setter
    def value(self, val: chr) -> None:
        self.__setitem__(self._position, val)

    def move_head(self, movement: Movement):
        self._position += movement.value
        if self._position not in range(0, self.__len__()):
            raise OutOfRangeError(self._position)

    def insert(self, __index: int, __object: chr):
        super().insert(int(__index), chr(__object))

    # def append(self, __object: chr):
    #     super().append(chr(__object))

    def extend(self, iterable):
        if isinstance(iterable, type(self)):
            super().extend(iterable)
        else:
            super().extend(chr(item) for item in iterable)

    def resize(self, new_size: int, empty_char: chr):
        if new_size <= self.__len__():
            return
        for i in range(new_size - self.__len__()):
            self.append(empty_char)

    def __str__(self):
        s = ""
        for i in range(self.__len__()):
            if i == self._position:
                s = s + FontStyle.RED + self[i] + FontStyle.END
            else:
                s = s + self[i]
        return s


class Tapes(list):
    type Values = tuple(str)
    type Movements = tuple(Movement)

    def append(self, value: Tape):
        super().append(value)

    def extend(self, iterable):
        if isinstance(iterable, type(self)):
            super().extend(iterable)
        else:
            super().extend(Tape(item) for item in iterable)

    @property
    def tape_values(self) -> Values:
        return tuple([tape.value for tape in self])

    @tape_values.setter
    def tape_values(self, values: Values):
        for i in range(0, self.__len__()):
            self[i].value = values[i]

    def move_heads(self, movements: Movements):
        for i in range(0, self.__len__()):
            self[i].move_head(movements[i])

    def resize_tapes(self, empty_char: chr):
        max_length = len(max(self, key=lambda x: x.__len__()))
        for tape in self:
            tape.resize(new_size=max_length, empty_char=empty_char)

    def __str__(self):
        s = ""
        for tape in self:
            s += str(tape) + "\n"
        return s


if __name__ == "__main__":
    _tapes = Tapes()
    _tapes.append(Tape("101"))
    _tapes[0].move(Movement.RIGHT)
    print(_tapes[0].value)
    _tapes[0].move(Movement.RIGHT)
    print(_tapes[0].value)
