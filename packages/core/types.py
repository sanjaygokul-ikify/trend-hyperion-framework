from typing import List, Dict

class TrendHyperionException(Exception):
    """
    Base exception for the trend-hyperion-framework
    """
    pass

class TrendHyperionTypeError(TrendHyperionException):
    """
    Exception raised when a type error occurs
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

class TrendHyperionValueError(TrendHyperionException):
    """
    Exception raised when a value error occurs
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)
