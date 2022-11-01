from fractions import Fraction

from Homeworks.OOP_S7Hw1.Loggers import logger


def check_value(value: str) -> float:
    try:
        try:
            value = float(value)
            return value
        except ValueError:
            value = Fraction(value)
            return value
    except ValueError:
        try:
            value = complex(value)
            return value
        except ValueError:
            logger.get_log("unknown result", "not correct value")
