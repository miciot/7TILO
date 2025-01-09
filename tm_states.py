class StartingStateError(Exception):
    def __init__(self, count):
        if count == 0:
            super().__init__(f"Missing starting state of machine")
        else:
            super().__init__(f"More than 1 ({count}) starting states of machine")


class EndingStateError(Exception):
    def __init__(self):
        super().__init__(f"Ending state of machine is missing")


class State:

    def __init__(self, state_id: any, starting: bool, ending: bool):
        self._starting = starting
        self._ending = ending
        self._id = state_id

    @property
    def starting(self) -> bool:
        return self._starting

    @property
    def ending(self) -> bool:
        return self._ending

    @property
    def id(self) -> any:
        return self._id


class States(dict[any, State]):
    def __init__(self, iterable=()):
        super().__init__(iterable)

    def get_starting(self) -> any:
        starting = [s.id for s in self.values() if s.starting]

        if len(starting) != 1:
            raise StartingStateError(len(starting))

        return starting[0]

    def get_ending(self) -> any:
        ending = [s.id for s in self.values() if s.ending]

        if len(ending) == 0:
            raise EndingStateError()

        return ending
