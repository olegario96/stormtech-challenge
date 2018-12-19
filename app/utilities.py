def binary_search(ordered_list, element, rules):
    index = int(len(ordered_list) / 2)
    if compare_books(ordered_list[index], element, rules):
        if index + 1 == len(ordered_list) - 1:
            if compare_books(ordered_list[index+1], element, rules):
                return len(ordered_list) - 1
            else:
                return len(ordered_list) - 2
        elif index + 1 >= len(ordered_list):
            return len(ordered_list) - 1
        elif compare_books(element, ordered_list[index+1], rules):
            return index
        else:
            return index + binary_search(ordered_list[index:], element, rules)
    else:
        if index - 1 == 0:
            if compare_books(element, ordered_list[index-1], rules):
                return - 1
            else:
                return 0
        elif index -  1 < 0:
            return -1
        elif compare_books(ordered_list[index-1], element, rules):
            return index - 1
        else:
            return binary_search(ordered_list[:index], element, rules)

def compare_books(b1, b2, rules):
    for key, value in rules.items():
        result = compare_books_by_one_attribute(b1, b2, key, value)
        if result != None:
            return result

def compare_books_by_one_attribute(b1, b2, attribute, desc=False):
    attribute_b1, attribute_b2 = b1.get(attribute), b2.get(attribute)
    min_len = min(len(attribute_b1), len(attribute_b2))
    result = None
    for i in range(0, min_len):
        if attribute_b1[i] < attribute_b2[i]:
            result = True
            break
        elif attribute_b1[i] > attribute_b2[i]:
            result = False
            break

    if not desc:
        return result
    else:
        return not result

def get_rules_from_json(json_books):
    rules = {}
    for key, value in json_books.items():
        if 'sorting' in key:
            entry = key.split('sorting_')[-1]
            if value == 'ascending':
                desc = False
            else:
                desc = True
            rules[entry] = desc

    return rules

def sort_books(json_books, rules):
    result = []
    result.append(json_books['books'].pop(0))
    for book in json_books['books']:
        index = binary_search(result, book, rules)
        print(index)
        print(book)
        print(result)
        result.insert(index+1, book)

    return result
