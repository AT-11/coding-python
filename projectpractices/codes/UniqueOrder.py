def unique_in_order(iterable):
    last = ""
    items_list = []
    for item in iterable:
        if item == last:
            continue
        else:
            items_list.append(item)
            last = item
    return items_list


if __name__ == '__main__':
    print(unique_in_order('AAAABBBCCDAABBB'))
    # unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
