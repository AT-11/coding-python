import re


def count_letters_and_digits(s):
    counter = 0
    for item in s:
        if re.search(r'[a-zA-Z0-9]', item):
            counter = counter + 1
    return counter


if __name__ == '__main__':
    print(count_letters_and_digits("hel2!lo"))  # --> 6
