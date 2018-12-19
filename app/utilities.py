def binary_search(ordered_list, element):
    index = int(len(ordered_list) / 2)
    if ordered_list[index] < element:
        if index + 1 == len(ordered_list):
            if ordered_list[index] < element:
                return len(ordered_list) - 1
            else:
                return len(ordered_list) - 2
        elif index + 1 > len(ordered_list):
            return len(ordered_list) - 1
        elif ordered_list[index+1] > element:
            return index
        else:
            return index + binary_search(ordered_list[index:], element)
    else:
        if index - 1 == 0:
            if ordered_list[index-1] > element:
                return - 1
            else:
                return 0
        elif index -  1 < 0:
            return -1
        elif ordered_list[index-1] < element:
            return index - 1
        else:
            return binary_search(ordered_list[:index], element)
