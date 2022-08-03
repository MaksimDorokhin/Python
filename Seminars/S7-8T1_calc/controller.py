import view
import calc
from logger import logger

def button() ->float:
    logger('start')
    a = view.input_num()
    logger(f'input a = {a}')
    operation = view.input_operation()
    logger(f'input operation = {operation}')
    b = view.input_num()
    logger(f'input b = {b}')
    
    match operation:
        case '+':
            view.print_result(a,b,operation,calc.sum(a,b))
            logger('Result = ' + str(calc.sum(a,b)))
        case '-':
            view.print_result(a,b,operation,calc.sub(a,b))
            logger('Result = ' + str(calc.sub(a,b)))
        case '*':
            view.print_result(a,b,operation,calc.mult(a,b))
            logger('Result = ' + str(calc.mult(a,b)))
        case '/':
            view.print_result(a,b,operation,calc.div(a,b))
            logger('Result = ' + str(calc.div(a,b)))
