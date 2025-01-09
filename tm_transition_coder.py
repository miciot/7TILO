from tm_transitions import *


class TuringMachineTansitionCoder:
    _current_state: int
    _new_state: int
    _current_values: Tapes.Values
    _new_values: Tapes.Values
    _movements: Tapes.Movements
    _tapes_count: int

    def __init__(self, separator: str = '1', value: str = '0'):
        # self._separator = '11'
        self._separator = separator
        self._value = value

    def decode(self, code: str) -> None:
        sections = code.split(self._separator)

        try:
            self._tapes_count = int((len(sections) - 2) / 3)
        except TypeError:
            pass

        self._current_state = int(len(sections[0]))
        self._current_values = [len(section) for section in sections[1:self._tapes_count + 1]]
        self._new_state = int(len(sections[self._tapes_count + 2]))
        self._new_values = [len(section) for section in sections[self._tapes_count + 2: 3 * self._tapes_count]]
        self._movements = [len(section) for section in sections[3 * self._tapes_count: 4 * self._tapes_count]]
        return None


if __name__ == '__main__':
    c = TuringMachineTansitionCoder()
    c.decode('01001010010010100100')
