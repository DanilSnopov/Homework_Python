from Letter_counter import counter
import pytest


tests = [("ANKJNkj kmjoijoijOIJOIJoiHHOIHJOIHOUB ygytf", '66%'), ('osjgdoi OUHUYG uigyUYYIkhsrjrr', '33%')]


@pytest.mark.parametrize('inp, result', tests)
def test_counter(inp, result):
    assert counter(inp) == result
