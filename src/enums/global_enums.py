from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = 'Resived status code is not eqaul to expected'
    WRONG_ELEMENT_COUNT = 'Number of items is not eqaul to expected'