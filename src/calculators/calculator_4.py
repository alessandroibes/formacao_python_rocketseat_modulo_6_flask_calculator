from flask import Request as FlaskRequest
from typing import Dict, List

from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator4:
    '''
    Calculadora 4

    * N números são colocados como entrada.

    * Retorna a média entre a lista de números fornecida.
    '''

    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)

        average = self.__calculate_average(input_data)

        formatted_response = self.__format_response(average)
        return formatted_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado!")
        
        input_data = body["numbers"]
        return input_data
    
    def __calculate_average(self, numbers: List[float]) -> float:
        average = self.__driver_handler.average(numbers)
        return average

    def __format_response(self, average: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "result": average
            }
        }
