# Вычислить число Pi c заданной точностью d
# Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


def get_int_accuracy_from_float_input(floatt: float) ->int:
    i = 0
    while floatt < 1:
        floatt*=10
        i+=1
    return i

def find_pi_with_specified_accuracy(accuracy: int) ->float:
    pi = 0
    for k in range (0, accuracy):
        pi += (1 / (16 ** k)) * ((4 / (8 *k + 1)) - (2 / (8 * k + 4)) - (1 / (8 * k + 5)) - (1 / (8 * k + 6)))
    return pi

correct_input = False

while not correct_input:
    try:
        d = float(input('\nВведите точность от 0.1 до 0.0000000001\n'))
        if (10**(-10) <= d <= 10**(-1)): correct_input = True
        else: print('\nВведенная точность вне заданного диапазона, попробуйте еще раз!')
    except:
        print('\nВведены недопустимые символы, попробуйте еще раз!')

accuracy = get_int_accuracy_from_float_input(d)
print(f'\nЧисло Пи с точностью до {accuracy} знаков равно:')
print(f'\n {round(find_pi_with_specified_accuracy(accuracy), accuracy)}\n')