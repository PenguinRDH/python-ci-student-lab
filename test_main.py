from main import add


def test_add():
    assert add(3, 2) == 5
    assert add(3, 3) == 6
