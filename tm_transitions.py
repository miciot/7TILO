from tm_tapes import *


class TransitionKey:
    state: int
    values: Tapes.Values

    def __init__(self, state: int, values: Tapes.Values):
        self.state = state
        self.values = values

    def get(self):
        return [self.state, self.values]


class TransitionValue:
    state: int
    values: Tapes.Values
    movements: Tapes.Movements

    def __init__(self, state: int, values: Tapes.Values, movements: Tapes.Movements):
        self.state = state
        self.values = values
        self.movements = movements

    def get(self):
        return [self.state, self.values, self.movements]


class Transition:
    type Key = tuple[any, Tapes.Values]
    type Value = tuple[any, Tapes.Values, Tapes.Movements]

    _current_state: any
    _current_values: Tapes.Values
    _new_state: any
    _new_values: Tapes.Values
    _movements: Tapes.Movements

    def __init__(self, current_state: any, current_values: Tapes.Values, new_state: any,
                 new_values: Tapes.Values, movements: Tapes.Movements):
        self._current_state = current_state
        self._current_values = current_values
        self._new_state = new_state
        self._new_values = new_values
        self._movements = movements

    @property
    def key(self):
        return self._current_state, self._current_values

    @property
    def value(self):
        return self._new_state, self._new_values, self._movements

    @property
    def current_state(self) -> any:
        return self._current_state

    @property
    def current_values(self) -> Tapes.Values:
        return self._current_values

    @property
    def new_state(self) -> any:
        return self._new_state

    @property
    def new_values(self) -> Tapes.Values:
        return self._new_values

    @property
    def movements(self) -> Tapes.Movements:
        return self._movements

    def __str__(self):
        s = f"\u03B4({self._current_state}"
        for value in self._current_values:
            s += f", {value}"
        s += f") = ({self._new_state}"
        for value in self._new_values:
            s += f", {value}"
        for movement in self._movements:
            s += f", {movement.name}"
        s += f")"
        return s


class Transitions(dict[Transition.Key, Transition]):
    def append(self, transition: Transition) -> None:
        self[transition.key] = transition

    def get_transition(self, key: Transition.Key) -> Transition:
        return self.__getitem__(key)

    def get_all_values(self) -> Tapes.Values:
        vals = []
        for value in self.values():
            vals.extend(value.new_values)
            vals.extend(value.current_values)
        return vals

    def get_all_states(self):
        states = []
        for value in self.values():
            states.extend(value.current_state)
            states.extend(value.new_state)
        return states
