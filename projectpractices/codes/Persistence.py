def persistence(n):
    suma = 1
    counter = 0
    while len(str(n)) > 1:
        counter = counter + 1
        suma = 1
        for digit in str(n):
            suma *= int(digit)
        n = suma
    print(suma)
    print(counter)


if __name__ == '__main__':
    persistence(39)