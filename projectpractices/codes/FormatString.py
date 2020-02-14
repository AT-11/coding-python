def namelist(names):
    size = len(names)
    cont = 0
    names_r = ""
    for key in names:
        names_r += key.get("name")
        cont = cont + 1
        if cont < size - 1:
            names_r += ', '
            continue
        elif cont == size:
            break
        else:
            names_r += " & "
    return names_r


if __name__ == '__main__':
    list = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
    print(namelist(list))
    # returns 'Bart, Lisa & Maggie'
