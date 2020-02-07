def persistence(n):
    # your code
    if n < 10:
        return 0
    n_str = str(n)
    multiply = 1
    for i in n_str:
        multiply = multiply * int(i)
    return 1 + persistence(multiply)

print(persistence(999))