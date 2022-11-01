from Homeworks.OOP_S7Hw1.Controllers.controller import Controller
from Homeworks.OOP_S7Hw1.Logic.chose_logic_factory import ChoseModelFactory
from Homeworks.OOP_S7Hw1.Views.view import View

pr = Controller(ChoseModelFactory(), View()).button_click()
