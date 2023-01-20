from app import bubblesort
import pytest

test_data = [
    ([4, 3, 6, 5, 2], [2, 3, 4, 5, 6]),
    ([2, 8, 7, 10], [2, 7, 8, 10]),
    ([9, 19, 2, 18, 5], [2, 5, 9, 18, 19]),
    (['e', 'r', 'r', 'o', 'r'], ['1']),
    ([4, 1, 17, 9], [1, 2, 3]),
    (1, 3)
]


@pytest.mark.parametrize('list_to_test, expected_list', test_data)
def test_bubblesort(list_to_test, expected_list):
    assert type(list_to_test) == list
    assert type(expected_list) == list
    assert [type(i) for i in list_to_test] == [int] * len(list_to_test)
    assert [type(i) for i in expected_list] == [int] * len(expected_list)
    assert len(list_to_test) == len(expected_list)

    bubble_list = bubblesort(list_to_test)[0]
    assert bubble_list == expected_list
