"""
    This files containg some functions to help the service
    sort all the books send by the client. The main function
    for this file is the binary search that, using a ordered
    of books, a book and the rules to ordenate, will return
    the index - 1 where the book should by inserted.
"""

def binary_search(ordered_list, element, rules):
    """
        This function implements a binary search on a
        ordered list. With a orderd list of books, a brand new
        book and a list of rules, this function will return
        the index -1 where the book should be inserted. This
        algorithm doesn't consider repeated elements. This
        algorithm has a performance of O(logn).
    """
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
    """
        Given two books and a list of rules, will return
        True in case of b1 has more priority according
        to the rules, and false, otherwise. The order
        of the rules can affect the result. In case
        of equal books, will return None.
    """
    for key, value in rules.items():
        result = compare_books_by_one_attribute(b1, b2, key, value)
        if result != None:
            return result

def compare_books_by_one_attribute(b1, b2, attribute, desc=False):
    """
        This function compare two books using one of its attributes.
        As the only sorting criteria is the alphabetical, both of
        attributes are compared char by char. The default value for
        ordering is ascending. With the ordering value is descending,
        the function just invert the final answer, saying that first
        book has less priority than second, or vice-versa.
    """
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
    """
        This function get all the rules from the
        JSON data sent by the client. An example
        of the JSON can be checked at the books.json
        file. For each key that has the 'sorting_' string,
        will check if its value if is ascending. If so,
        will mark the rule as no descending, and true
        otherwise. Every 'sorting_' string must be succeeded
        with one of the books attribute.
    """
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
    """
        This function sort the books that cames from the JSON
        data sent by the client, and its rules. Will take
        the first book of the list, add to the list, and
        start the process to compare and insert in order
        into the list. At end, return the list ordered with
        the books, using as criteria the rules.
    """
    result = []
    result.append(json_books.get('books').pop(0))
    for book in json_books.get('books'):
        index = binary_search(result, book, rules)
        result.insert(index+1, book)

    return result
