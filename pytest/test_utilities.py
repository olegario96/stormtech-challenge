from app.utilities import binary_search
import pytest
import random

@pytest.fixture(scope='session')
def random_list():
    random_list = random.sample(range(0, 100), 10)
    random_list.sort()
    return random_list

def test_binary_search(random_list):
    element = random.randint(1, 100)
    index_from_search = binary_search(random_list, element)
    while element in random_list:
        element = random.randint(1, 100)

    print(element)
    print(random_list)
    for i in range(0, len(random_list)):
        if random_list[i] > element:
            assert i - 1  == index_from_search
            break
