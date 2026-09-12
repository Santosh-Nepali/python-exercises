def count_up_to(n):
    for number in range(1, n + 1):
        yield number
count_up_to(7)