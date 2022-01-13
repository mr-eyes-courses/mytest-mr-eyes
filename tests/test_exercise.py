import pytest
from src.exercise import Excercise
def test_verify_message():
    EX = Excercise()
    assert EX.hello() == "asasas"