from LetterCounter import lettercounter
import pytest


tests = [("ANKJNkj kmjoijoijOIJOIJoiHHOIHJOIHOUB ygytf", '66%'), ('osjgdoi OUHUYG uigyUYYIkhsrjrr', '33%')]


@pytest.mark.parametrize('inp, result', tests)
def test_counter(inp, result):
    """Прогоняет тесты по импортированной функции."""
    assert lettercounter(inp) == result
