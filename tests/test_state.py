
from hypothesis import strategies as st
from hypothesis.stateful import RuleBasedStateMachine, invariant, rule


class DataStore:
    def __init__(self):
        self.records = {}

    def insert(self, key, value):
        self.records[key] = value

    def delete(self, key):
        self.records.pop(key, None)

    def update(self, key, value):
        if key in self.records:
            self.records[key] = value

class DataStoreMachine(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.store = DataStore()
        self.model = {}

    @rule(key=st.text(min_size=1, max_size=3), value=st.integers())
    def insert(self, key, value):
        self.store.insert(key, value)
        self.model[key] = value

    @rule(key=st.text(min_size=1, max_size=3))
    def delete(self, key):
        self.store.delete(key)
        self.model.pop(key, None)

    @rule(key=st.text(min_size=1, max_size=3), value=st.integers())
    def update(self, key, value):
        self.store.update(key, value)
        if key in self.model:
            self.model[key] = value

    @invariant()
    def store_matches_model(self):
        assert self.store.records == self.model


TestDataStore = DataStoreMachine.TestCase
