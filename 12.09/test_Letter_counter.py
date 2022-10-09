
from Letter_counter import lettercounter
import pytest


tests = [("ANKJNkj kmjoijoijOIJOIJoiHHOIHJOIHOUB ygytf", '66%'), ('osjgdoi OUHUYG uigyUYYIkhsrjrr', '33%')]


@pytest.mark.parametrize('inp, resultat', tests)
def test_counter(inp, resultat):
    """Прогоняет тесты по импортированной функции."""
    assert lettercounter(inp) == resultat
