from flask import Request as FlaskRequest
from typing import Dict


class Calculator1:

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        splited_number = input_data / 3

        first_process_result = self.__first_process(splited_number)

        print(input_data)

    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise Exception("body nal formatado!")
        
        input_data = body["number"]
        return input_data
    
    def __first_process(self, first_number: float) -> float:
        first_part = (first_number / 4) + 7
        second_part = (first_part ** 2) * 0.257
        return second_part
