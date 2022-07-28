import view
import calc

def button() ->float:

    a = view.input_num()
    operation = view.input_operation()
    b = view.input_num()
    
    match operation:
        case '+':
            view.print_result(a,b,operation,calc.sum(a,b))
        case '-':
            view.print_result(a,b,operation,calc.sub(a,b))
        case '*':
            view.print_result(a,b,operation,calc.mult(a,b))
        case '/':
            view.print_result(a,b,operation,calc.div(a,b))
            
