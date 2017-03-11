

import pytest

from mafia_game.role import Role


@pytest.fixture
def r():
    r = Role("A", "B", "C")
    return r


def test_create_role(r):
    assert r.role_name == "A"
    assert r.role_allegiance == "B"
    assert r.role_verdict == "C"


def test_role_stringification(r):
    assert str(r) == "[0] A {B, C}"
