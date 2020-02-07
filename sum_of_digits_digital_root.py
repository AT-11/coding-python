def digital_root(n):
    # ...
    digits = 0
    add_digits = 0
    while n != 0:
        digits = n % 10
        n //= 10
        add_digits += digits
    if add_digits > 9:
        return digital_root(add_digits)
    return add_digits

print (digital_root(942))