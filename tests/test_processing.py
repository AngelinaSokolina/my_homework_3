import pytest


from src.processing import filter_by_state, sort_by_date

"""Тест для функции, которая фильтрует список словарей по значению ключа 'state'."""
@pytest.mark.parametrize("data_filter, state_to_find, expected_filter", [
    # 1. Проверка правильности фильтра (Ожидаем СПИСОК с одним словарем)
    (
        [{'id': 1, 'state': 'EXECUTED', 'date': '2019-07-03'}, {'id': 2, 'state': 'CANCELED', 'date': '2018-06-30'}],
        'EXECUTED',
        [{'id': 1, 'state': 'EXECUTED', 'date': '2019-07-03'}]
    ),

    # 2. Отсутствие статуса (Ожидаем пустой список)
    (
        [{'id': 2, 'state': 'CANCELED', 'date': '2018-06-30'}],
        'EXECUTED',
        []
    ),

    # 3. Пустой входной список
    (
            [], 'EXECUTED', []
    ),
])
def test_filter_by_state(data_filter, state_to_find, expected_filter):
    assert filter_by_state(data_filter, state_to_find) == expected_filter


"""
Тест для функции сортировки списка словарей по ключу 'date'.
По умолчанию сортировка идет от новых к старым (убывание).
"""
@pytest.mark.parametrize("data_sort, is_reverse, expected_sort", [
    # 1. Проверка правильности сортировки по убыванию
    (
        [{'id': 1, 'date': '2019-07-03'}, {'id': 2, 'date': '2018-06-30'}],
        True,
        [{'id': 1, 'date': '2019-07-03'}, {'id': 2, 'date': '2018-06-30'}]
    ),
    # 2. Проверка правильности сортировки по возрастанию
    (
        [{'id': 1, 'date': '2019-07-03'}, {'id': 2, 'date': '2018-06-30'}],
        False,
        [{'id': 2, 'date': '2018-06-30'}, {'id': 1, 'date': '2019-07-03'}]
    ),
    # 3. Проверка одинаковых дат
    (
        [{'id': 1, 'date': '2020-07-03'}, {'id': 2, 'state': 'CANCELED', 'date': '2018-06-30'},
        {'id': 3, 'date': '2020-07-03'}],
        False,
        [{'id': 2, 'state': 'CANCELED', 'date': '2018-06-30'}, {'id': 1, 'date': '2020-07-03'},
        {'id': 3, 'date': '2020-07-03'}]
    ),
])
def test_sort_by_date(data_sort, is_reverse, expected_sort):
    assert sort_by_date(data_sort, reverse = is_reverse) == expected_sort

"""Дополнительный маленький тест для сортировки, 
когда ожидаем, что внутри этого блока возникнет KeyError"""
def test_sort_by_date_errors():
    with pytest.raises(KeyError):
        # Передаем список, где у одного словаря нет ключа 'date'
        sort_by_date([{'id': 1, 'date': '2023'}, {'id': 2}], reverse=True)



