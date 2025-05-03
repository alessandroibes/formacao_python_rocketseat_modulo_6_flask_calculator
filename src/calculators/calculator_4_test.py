from pytest import raises
from typing import Dict, List

from .calculator_4 import Calculator4
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler:
    def average(self, numbers: List[float]) -> float:
        return 3.0


def test_calculator():
    mock_request = MockRequest({ "numbers": [1, 2, 3, 4, 5] })
    calculator_4 = Calculator4(MockDriverHandler())

    response = calculator_4.calculate(mock_request)
    
    assert response == {
        "data": {
            "Calculator": 4,
            "result": 3.0
        }
    }


def test_calculator_unprocessable_entity_error():
    mock_request = MockRequest({ "values": [1, 2, 3, 4, 5] })
    calculator_4 = Calculator4(MockDriverHandler())

    with raises(HttpUnprocessableEntityError) as excinfo:
        calculator_4.calculate(mock_request)

    assert str(excinfo.value) == "body mal formatado!"
