from tm_coder import *
from abc import ABC, abstractmethod


class TransitionStateError(Exception):
    def __init__(self, state_ids: list[int]):
        super().__init__(f"States {state_ids} are not in set of states")


class TransitionValuesError(Exception):
    def __init__(self, incorrect: list[chr]):
        super().__init__(f"Values from transition rule {incorrect} are not in alphabet")


class AlphabetContainsEmptyError(Exception):
    def __init__(self, empty_char: chr):
        super().__init__(f"Alphabet contains empty symbol {empty_char}")


class ContentOutOfAlphabetError(Exception):
    def __init__(self, tape: int, invalid: list[chr]):
        super().__init__(
            f"Tape {tape} contains characters not included in alphabet:\n{invalid}"
        )


class TransitionNotFound(Exception):
    def __init__(self, state: int, values: Tapes.Values):
        super().__init__(f"Transition not found for state {state} and values {values}")


class ValidCharactersNotFound(Exception):
    def __init__(self, tape: int):
        super().__init__(f"Valid characters were not found on tape {tape}")


class EndingStateReached(Exception):
    pass


class TuringMachineConfig(ABC):
    _active_tape: int
    _states: States
    _transitions: Transitions
    _tapes: Tapes
    _alphabet: Alphabet
    _empty_char: chr

    def __init__(self):
        self._states: States = self.get_states()
        self._transitions = self.get_transitions()
        self._tapes = self.get_tapes()
        self._alphabet = self.get_alphabet()
        self._empty_char = self.get_empty_char()

    def __str__(self) -> str:
        ret = self.get_transitions_coder().encode(
            states=self._states,
            alphabet=self._alphabet,
            empty_char=self._empty_char,
            transitions=self._transitions,
        )
        return ret

    def get_transitions_coder(self) -> TuringMachineCoder:
        return TuringMachineCoder()

    @property
    def empty_char(self) -> chr:
        return self._empty_char

    @property
    def alphabet(self) -> Alphabet:
        return self._alphabet

    @property
    def states(self) -> States:
        return self._states

    @property
    def tapes(self) -> Tapes:
        return self._tapes

    @property
    def transitions(self) -> Transitions:
        return self._transitions

    @abstractmethod
    def get_tapes(self) -> Tapes:
        pass

    @abstractmethod
    def get_transitions(self) -> Transitions:
        pass

    @abstractmethod
    def get_states(self) -> States:
        pass

    @abstractmethod
    def get_alphabet(self) -> Alphabet:
        pass

    @abstractmethod
    def get_empty_char(self) -> chr:
        pass


class TuringMachine:
    _state: int
    _states: States
    _transitions: Transitions
    _tapes: Tapes
    _alphabet: Alphabet
    _empty_char: chr

    def __init__(
        self,
        states: States,
        tapes: Tapes,
        transitions: Transitions,
        alphabet: Alphabet,
        empty_char: chr,
    ):
        self._empty_char = empty_char
        self._set_alphabet(alphabet)
        self._set_states(states)
        self._set_tapes(tapes)
        self._set_transitions(transitions)

    @staticmethod
    def __call__(self, config: TuringMachineConfig):
        machine = TuringMachine(
            states=config.states,
            tapes=config.tapes,
            transitions=config.transitions,
            alphabet=config.alphabet,
            empty_char=config.empty_char,
        )
        machine.iterate()

    def __str__(self):
        return f"State: {self._state}\n" + str(self._tapes)

    def _set_alphabet(self, alphabet: Alphabet):
        self._alphabet = alphabet

    def _set_states(self, states: States):
        states.get_ending()
        self._state = states.get_starting()
        self._states = states

    def _set_transitions(self, transitions: Transitions):
        unknown_states = [
            t.current_state
            for t in transitions.values()
            if t.current_state not in self._states.keys()
        ] + [
            t.new_state
            for t in transitions.values()
            if t.new_state not in self._states.keys()
        ]

        if len(unknown_states) > 0:
            raise TransitionStateError(unknown_states)

        incorrect_values = list()
        alphabet_set = set(self._alphabet)
        for t in transitions.values():
            incorrect_values.extend(set(t.current_values) - alphabet_set)
            incorrect_values.extend(set(t.new_values) - alphabet_set)
        if len(incorrect_values) > 0:
            raise TransitionValuesError(incorrect_values)

        self._transitions = transitions

    def _write_info(self, transition: Transition):
        print(self)
        print(transition)
        print("-----------------------------------")

    def _set_tapes(self, tapes: Tapes):
        for tape in tapes:
            invalid = [i for i in tape if i not in self._alphabet]
            if len(invalid) > 1:
                raise ContentOutOfAlphabetError(tape.name, invalid)
            # try:
            #     while tape.value == self._empty_char:
            #         tape.move_head(Movement.RIGHT)
            # except OutOfRangeError:
            #     raise ValidCharactersNotFound(tape.name)
        self._tapes = tapes

    def _get_transition_key(self) -> Transition.Key:
        return self._state, self._tapes.tape_values

    def _get_transition(self) -> Transition:
        return self._transitions[self._get_transition_key()]

    def _iterate(self):
        transition: Transition | None = self._get_transition()

        if transition is None:
            raise TransitionNotFound(self._state, self._tapes.tape_values)

        self._write_info(transition)

        self._tapes.tape_values = transition.new_values
        self._tapes.move_heads(transition.movements)
        self._state = transition.new_state

        if self._states[self._state].ending:
            raise EndingStateReached

        self._iterate()

    def iterate(self):
        try:
            self._tapes.resize_tapes(empty_char=self._empty_char)
            print(f"Input:")
            for tape in self._tapes:
                if tape.input:
                    print(tape)
            print()
            self._iterate()
        except EndingStateReached:
            print()
            print(f"Output:")
            for tape in self._tapes:
                if tape.output:
                    print(tape)
            return
        except Exception as ex:
            print(ex)
        finally:
            pass
