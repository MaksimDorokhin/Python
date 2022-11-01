from Homeworks.OOP_S7Hw1.Loggers import logger
from Homeworks.OOP_S7Hw1.Logic.chose_logic_factory import ChoseModelFactory
from Homeworks.OOP_S7Hw1.Logic.value_checker import check_value
from Homeworks.OOP_S7Hw1.Views.view import View


class Controller:
    calc = ChoseModelFactory()
    view = View()

    def __init__(self, calc, view):
        self.calc = calc
        self.view = view

    def button_click(self):
        a = check_value(self.view.get_value("first number"))
        sign = self.view.get_sign("math char")
        b = check_value(self.view.get_value("second number"))
        my_list = [a, b]
        c = self.calc.choose_model(sign, my_list).result()
        strr = f"{a} {sign} {b} = {c}"
        View.show_result(strr)
        logger.get_log(c, f"{a} {sign} {b}")
