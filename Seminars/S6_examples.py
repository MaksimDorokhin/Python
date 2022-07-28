for row in matrix:
    for item in row:
        ''.join('{:4}'.format(item))
    print('\n')