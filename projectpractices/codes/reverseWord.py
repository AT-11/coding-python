def solution(string):
    result = ""
    size = len(string)
    while size > 0:
        size = size - 1
        result += string[size]
    return result


if __name__ == '__main__':
    print(solution('world'))
    # returns 'dlrow'
