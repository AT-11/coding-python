def digital_root(n):
    sumas = 0
    while n:
        number = int(n % 10)
        sumas += number
        n = int(n / 10)
    if sumas > 9:
        return digital_root(sumas)
        print(sumas)
    else:
        print(sumas)


if __name__ == '__main__':
    digital_root(493193)