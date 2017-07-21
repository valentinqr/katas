def iterative_chop(search_value, search_list):
    found_at = -1
    for idx, val in enumerate(search_list):
        if val == search_value:
            found_at = idx
    return found_at


def builtin_chop(search_value, search_list):
    try:
        return search_list.index(search_value)
    except:
        return -1


def recursive_chop(search_value, search_list):
    if search_value not in search_list:
        return -1
    if search_list[0] == search_value:
        return 0
    else:
        return 1 + recursive_chop(search_value, search_list[1:])
