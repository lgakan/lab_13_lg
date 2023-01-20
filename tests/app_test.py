from app import bubblesort
import pytest

test_correct_data = [
    ([4, 3, 6, 5, 2], [2, 3, 4, 5, 6]),
    ([2, 8, 7, 10], [2, 7, 8, 10]),
    ([9, 19, 2, 18, 5], [2, 5, 9, 18, 19])
]
test_incorrect_type_data = [
    (['4', '3', '6', '5', '2'], ['2', '3', '4', '5', '6']),
    ([2.3, 2.1, 1, 1.4], [1, 1.4, 2.1, 2.3])]

test_incorrect_length_data = [
    ([4, 3, 6, 2], [2, 3, 4, 5, 6]),
    ([2, 8, 7, 10], [2, 7, 8])]

single_data = [('Random sentence to test', [1, 2, 3]),
               ('xxxx', [1, 2, 3])]

empty_data = ''


@pytest.mark.parametrize('list_to_test, expected_list', test_correct_data)
def test_correct_bubblesort(list_to_test, expected_list):
    bubble_list = bubblesort(list_to_test)[0]
    assert bubble_list == expected_list


@pytest.mark.parametrize('list_to_test, expected_list', test_incorrect_type_data)
def test_incorrect_type_bubblesort(list_to_test, expected_list):
    assert [type(i) for i in list_to_test] == [int] * len(list_to_test)
    assert [type(i) for i in expected_list] == [int] * len(expected_list)
    bubble_list = bubblesort(list_to_test)[0]
    assert bubble_list == expected_list


@pytest.mark.parametrize('list_to_test, expected_list', test_incorrect_length_data)
def test_incorrect_length_bubblesort(list_to_test, expected_list):
    assert len(list_to_test) == len(expected_list)
    bubble_list = bubblesort(list_to_test)[0]
    assert bubble_list == expected_list


@pytest.mark.parametrize('list_to_test, expected_list', single_data)
def test_single_string_bubblesort(list_to_test, expected_list):
    assert type(list_to_test) == list
    bubble_list = bubblesort(list_to_test)[0]
    assert bubble_list == expected_list


@pytest.mark.parametrize('list_to_sort', empty_data)
def test_if_empty_bubblesort(list_to_sort):
    assert len(list_to_sort) != 0
    bubble_list = bubblesort(list_to_sort)[0]
    assert bubble_list == list_to_sort
