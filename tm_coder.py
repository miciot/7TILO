from tm_transitions import *
from tm_states import *
from tm_common import *
from tm_alphabet import *


class TuringMachineCoder:
    _states: States
    _alphabet: Alphabet
    _transitions: Transitions
    _empty_char: chr

    def __init__(self):
        self._begin_end = '111'
        self._separator = '11'
        self._transition_separator = '1'
        self._value = '0'

    def encode(self, states: States, alphabet: Alphabet, empty_char: chr, transitions: Transitions) -> str:
        self._states = states
        self._alphabet = alphabet
        self._transitions = transitions
        self._empty_char = empty_char

        ret = ""
        ret += self._begin_end
        ret += self.encode_alphabet()
        ret += self._separator
        ret += self.encode_states()
        ret += self._separator
        ret += self.encode_transitions()
        ret += self._begin_end
        return ret

    def decode(self, code: str):
        transition_codes = code.split(self._begin_end)[1].split(self._separator)
        transitions = Transitions()

        for transition_code in transition_codes:
            transitions.append(self.parse_transition(transition_code))

    def parse_transition(self, code: str) -> Transition:
        tcnt: int
        sections = code.split(self._transition_separator)

        tcnt = int((sections.__len__() - 2)/3)

        index = 0
        current_state = sections[index]
        index += 1
        current_values = sections[index:tcnt + index]
        index = tcnt + index + 1
        new_state = sections[index]
        index += 1
        new_values = sections[index:tcnt + index]
        index = tcnt + index
        movements = sections[index:tcnt + index]

        return Transition(current_state=current_state, current_values=current_values, new_state=new_state,
                          new_values=new_values, movements=movements)

        pass

    def encode_states(self) -> str:
        ret = self.__get_value(len(self._states))
        ret += self._separator
        ret += self.__get_value(self._states.get_starting())
        ret += self._transition_separator
        for state_id in self._states.get_ending():
            ret += self.__get_value(state_id)
        return ret

    def encode_alphabet(self) -> str:
        return self.__get_value(len(self._alphabet))

    def encode_transitions(self) -> str:
        ret = ""
        for transition_key in self._transitions.keys():
            transition = self._transitions.get_transition(transition_key)
            ret += self.encode_transition(transition)
        return ret

    def encode_transition(self, transition: Transition) -> str:
        ret = ""
        ret += self.__get_value(transition.current_state + 1)

        for value in transition.current_values:
            ret += self.__get_value(self._alphabet.index(value) + 1)

        ret += self.__get_value(transition.new_state + 1)

        for value in transition.new_values:
            ret += self.__get_value(self._alphabet.index(value) + 1)

        for idx, movement in enumerate(transition.movements):
            if movement == Movement.LEFT:
                i = 1
            elif movement == Movement.RIGHT:
                i = 2
            else:
                i = 3
            ret += self.__get_value(i, idx == (transition.movements.__len__() - 1))

        ret += self._separator
        return ret

    def __get_value(self, cnt: int, skip_separator: bool = False) -> str:
        ret = ''
        for _ in range(cnt):
            ret += self._value
        if not skip_separator:
            ret += self._transition_separator
        return ret

    def clean(self):
        self._c
