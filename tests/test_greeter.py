from src.greeter import Greeter


def test_greeting():
    assert 'Hello, Hands.' == Greeter.greet('hands')
