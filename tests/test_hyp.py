
from hypothesis import given
from hypothesis import strategies as st

NUM_LIMIT = 2**53

@given(st.lists(st.integers()))
def test_reverse_twice_is_original(xs):
    assert list(reversed(list(reversed(xs)))) == xs

def average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list.")
    if abs(sum(numbers)) > NUM_LIMIT or abs(len(numbers)) > NUM_LIMIT:
        raise ValueError("Precision Lost")
    return sum(numbers) / len(numbers)

rand_vals = st.lists(st.integers(min_value=1, max_value=1000), min_size=1, max_size=NUM_LIMIT)

@given(rand_vals)
def test_average(numbers):
    result = average(numbers)
    assert min(numbers) <= result <= max(numbers)
