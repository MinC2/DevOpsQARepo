import pytest
from helloWorld import *
def test_helloWorld_NoInput():
    result = helloWorld()
    assert result == "Hello World!" #this is to check if result returns hello world!

@pytest.mark.parametrize("name, expectedResult", #pass in input, expected result
[("Danny", "Hello Danny!"), ("Caleb", "Hello Caleb!"),#pass in input, expected result
("Eugene", "Hello Eugene!")])

def test_helloWorld_UserInput(name, expectedResult):
    result = helloWorld(name)
    assert result == expectedResult