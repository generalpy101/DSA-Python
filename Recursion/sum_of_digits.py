# only supports positive integers
def sum_of_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)


if __name__ == "__main__":
    print(sum_of_digits(223))