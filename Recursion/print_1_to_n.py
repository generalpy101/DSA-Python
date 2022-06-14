def print_1_to_n(n) :
    if n == 0 : return
    print_1_to_n(n-1)
    print(n)


if __name__ == '__main__':
    print_1_to_n(10)