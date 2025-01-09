import sys
import os
from tm import *


class TestConfig(TuringMachineConfig):
    def __init__(self, _input: str):
        self._input = _input
        super().__init__()

    def get_tapes(self) -> Tapes:
        tapes = Tapes()
        tapes.append(Tape(self._input, _input=True))
        tapes.append(Tape(_output=True))
        return tapes

    def get_transitions(self) -> Transitions:
        transitions = Transitions()

        transitions.append(
            Transition(current_state=0, current_values=tuple(['0', '#']), new_state=1, new_values=tuple(['0', '#']),
                       movements=[Movement.RIGHT, Movement.RIGHT]))
        transitions.append(
            Transition(current_state=0, current_values=tuple(['1', '#']), new_state=1, new_values=tuple(['1', '#']),
                       movements=[Movement.RIGHT, Movement.RIGHT]))
        transitions.append(
            Transition(current_state=0, current_values=tuple(['#', '#']), new_state=0, new_values=tuple(['#', '#']),
                       movements=[Movement.RIGHT, Movement.RIGHT]))
        transitions.append(
            Transition(current_state=1, current_values=tuple(['0', '#']), new_state=1, new_values=tuple(['0', '#']),
                       movements=[Movement.RIGHT, Movement.RIGHT]))
        transitions.append(
            Transition(current_state=1, current_values=tuple(['1', '#']), new_state=1, new_values=tuple(['1', '#']),
                       movements=[Movement.RIGHT, Movement.RIGHT]))
        transitions.append(
            Transition(current_state=1, current_values=tuple(['#', '#']), new_state=2, new_values=tuple(['#', '#']),
                       movements=[Movement.RIGHT, Movement.RIGHT]))
        transitions.append(
            Transition(current_state=2, current_values=tuple(['0', '#']), new_state=1, new_values=tuple(['0', '#']),
                       movements=[Movement.RIGHT, Movement.RIGHT]))
        transitions.append(
            Transition(current_state=2, current_values=tuple(['1', '#']), new_state=1, new_values=tuple(['1', '#']),
                       movements=[Movement.RIGHT, Movement.RIGHT]))
        transitions.append(
            Transition(current_state=2, current_values=tuple(['#', '#']), new_state=3, new_values=tuple(['#', '#']),
                       movements=[Movement.LEFT, Movement.LEFT]))
        transitions.append(
            Transition(current_state=3, current_values=tuple(['#', '#']), new_state=4, new_values=tuple(['#', '#']),
                       movements=[Movement.LEFT, Movement.LEFT]))
        transitions.append(
            Transition(current_state=4, current_values=tuple(['0', '#']), new_state=4, new_values=tuple(['#', '0']),
                       movements=[Movement.LEFT, Movement.LEFT]))
        transitions.append(
            Transition(current_state=4, current_values=tuple(['1', '#']), new_state=4, new_values=tuple(['#', '1']),
                       movements=[Movement.LEFT, Movement.LEFT]))
        transitions.append(
            Transition(current_state=4, current_values=tuple(['#', '#']), new_state=5, new_values=tuple(['#', '#']),
                       movements=[Movement.NONE, Movement.RIGHT]))
        transitions.append(
            Transition(current_state=5, current_values=tuple(['#', '0']), new_state=5, new_values=tuple(['#', '0']),
                       movements=[Movement.NONE, Movement.RIGHT]))
        transitions.append(
            Transition(current_state=5, current_values=tuple(['#', '1']), new_state=5, new_values=tuple(['#', '1']),
                       movements=[Movement.NONE, Movement.RIGHT]))
        transitions.append(
            Transition(current_state=5, current_values=tuple(['#', '#']), new_state=8, new_values=tuple(['#', '#']),
                       movements=[Movement.LEFT, Movement.LEFT]))
        transitions.append(
            Transition(current_state=6, current_values=tuple(['0', '0']), new_state=6, new_values=tuple(['#', '0']),
                       movements=[Movement.LEFT, Movement.LEFT]))
        transitions.append(
            Transition(current_state=6, current_values=tuple(['0', '1']), new_state=6, new_values=tuple(['#', '1']),
                       movements=[Movement.LEFT, Movement.LEFT]))
        transitions.append(
            Transition(current_state=6, current_values=tuple(['0', '#']), new_state=6, new_values=tuple(['#', '0']),
                       movements=[Movement.LEFT, Movement.LEFT]))
        transitions.append(
            Transition(current_state=6, current_values=tuple(['1', '0']), new_state=6, new_values=tuple(['#', '1']),
                       movements=[Movement.LEFT, Movement.LEFT]))
        transitions.append(
            Transition(current_state=6, current_values=tuple(['1', '1']), new_state=7, new_values=tuple(['#', '0']),
                       movements=[Movement.LEFT, Movement.LEFT]))
        transitions.append(
            Transition(current_state=6, current_values=tuple(['1', '#']), new_state=6, new_values=tuple(['#', '1']),
                       movements=[Movement.LEFT, Movement.LEFT]))
        transitions.append(
            Transition(current_state=6, current_values=tuple(['#', '0']), new_state=8, new_values=tuple(['#', '0']),
                       movements=[Movement.LEFT, Movement.LEFT]))
        transitions.append(
            Transition(current_state=6, current_values=tuple(['#', '1']), new_state=8, new_values=tuple(['#', '1']),
                       movements=[Movement.LEFT, Movement.LEFT]))
        transitions.append(
            Transition(current_state=6, current_values=tuple(['#', '1']), new_state=8, new_values=tuple(['#', '1']),
                       movements=[Movement.LEFT, Movement.LEFT]))
        transitions.append(
            Transition(current_state=6, current_values=tuple(['#', '#']), new_state=5, new_values=tuple(['#', '#']),
                       movements=[Movement.NONE, Movement.RIGHT]))
        transitions.append(
            Transition(current_state=7, current_values=tuple(['0', '0']), new_state=6, new_values=tuple(['#', '1']),
                       movements=[Movement.LEFT, Movement.LEFT]))
        transitions.append(
            Transition(current_state=7, current_values=tuple(['0', '1']), new_state=7, new_values=tuple(['#', '0']),
                       movements=[Movement.LEFT, Movement.LEFT]))
        transitions.append(
            Transition(current_state=7, current_values=tuple(['1', '0']), new_state=7, new_values=tuple(['#', '0']),
                       movements=[Movement.LEFT, Movement.LEFT]))
        transitions.append(
            Transition(current_state=7, current_values=tuple(['1', '1']), new_state=7, new_values=tuple(['#', '1']),
                       movements=[Movement.LEFT, Movement.LEFT]))
        transitions.append(
            Transition(current_state=7, current_values=tuple(['#', '0']), new_state=5, new_values=tuple(['#', '1']),
                       movements=[Movement.NONE, Movement.RIGHT]))
        transitions.append(
            Transition(current_state=7, current_values=tuple(['#', '1']), new_state=7, new_values=tuple(['#', '0']),
                       movements=[Movement.NONE, Movement.LEFT]))
        transitions.append(
            Transition(current_state=7, current_values=tuple(['#', '#']), new_state=8, new_values=tuple(['#', '1']),
                       movements=[Movement.LEFT, Movement.LEFT]))
        transitions.append(
            Transition(current_state=8, current_values=tuple(['0', '#']), new_state=5, new_values=tuple(['0', '#']),
                       movements=[Movement.RIGHT, Movement.RIGHT]))
        transitions.append(
            Transition(current_state=8, current_values=tuple(['1', '#']), new_state=5, new_values=tuple(['1', '#']),
                       movements=[Movement.RIGHT, Movement.RIGHT]))
        transitions.append(
            Transition(current_state=8, current_values=tuple(['#', '0']), new_state=9, new_values=tuple(['#', '0']),
                       movements=[Movement.NONE, Movement.NONE]))
        transitions.append(
            Transition(current_state=8, current_values=tuple(['#', '1']), new_state=9, new_values=tuple(['#', '1']),
                       movements=[Movement.NONE, Movement.NONE]))
        transitions.append(
            Transition(current_state=8, current_values=tuple(['#', '#']), new_state=9, new_values=tuple(['#', '#']),
                       movements=[Movement.NONE, Movement.NONE]))
        transitions.append(
            Transition(current_state=8, current_values=tuple(['0', '1']), new_state=6, new_values=tuple(['0', '1']),
                       movements=[Movement.NONE, Movement.NONE]))
        transitions.append(
            Transition(current_state=8, current_values=tuple(['1', '0']), new_state=6, new_values=tuple(['1', '0']),
                       movements=[Movement.NONE, Movement.NONE]))
        transitions.append(
            Transition(current_state=8, current_values=tuple(['0', '0']), new_state=6, new_values=tuple(['0', '0']),
                       movements=[Movement.NONE, Movement.NONE]))
        transitions.append(
            Transition(current_state=8, current_values=tuple(['1', '1']), new_state=6, new_values=tuple(['1', '1']),
                       movements=[Movement.NONE, Movement.NONE]))

        return transitions

    def get_states(self) -> States:
        states = States()
        states[0] = State(0, True, False)
        states[1] = State(1, False, False)
        states[2] = State(2, False, False)
        states[3] = State(3, False, False)
        states[4] = State(4, False, False)
        states[5] = State(5, False, False)
        states[6] = State(6, False, False)
        states[7] = State(7, False, False)
        states[8] = State(8, False, False)
        states[9] = State(9, False, True)
        return states

    def get_alphabet(self) -> Alphabet:
        alphabet = Alphabet()
        alphabet.extend("01")
        return alphabet

    def get_empty_char(self) -> chr:
        return "#"


if __name__ == "__main__":
    os.system("cls")
    os.system("")
    print(sys.argv)
    if sys.argv[1] == "":
        pass

    print("Binary coded:")
    config = TestConfig(sys.argv[1])
    print(config)
    print()
    tm = TuringMachine(states=config.get_states(), tapes=config.get_tapes(), alphabet=config.get_alphabet(),
                       transitions=config.get_transitions(), empty_char=config.get_empty_char())
    tm.iterate()
