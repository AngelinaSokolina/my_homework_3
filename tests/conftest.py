import pytest

@pytest.fixture
def operation_data():
    """Общая фикстура со списком для фильтрации и сортировки"""
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2024-03-11T02:26:18.671407'},
        {'id': 2, 'state': 'CANCELED', 'date': '2023-05-24T10:15:00.000000'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2025-01-01T00:00:00.000000'},
        {'id': 4, 'state': 'PENDING', 'date': '2022-12-31T23:59:59.999999'}
    ]

@pytest.fixture
def empty_list():
    """Фикстура для проверки пустого списка"""
    return []
