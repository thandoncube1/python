
def print_move(fr, to):
    print('Move from ' + str(fr) + ' to ' + str(to))


def tower(n, fr, to, spare):
    if n == 1:
        print_move(fr, to)
    else:
        tower(n-1, fr, spare, to)
        tower(1, fr, to, spare)
        tower(n-1, spare, to, fr)


def main():
    pass


main()
