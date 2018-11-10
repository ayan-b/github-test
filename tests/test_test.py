import pytest
from hello import hello

def test_demo():
    assert hello.hi() == "hi"