import pytest
from typing import Any, Dict, List
from src.generators import filter_by_currency


@pytest.fixture
def transactions() -> List[Dict[str, Any]]:
    """Фикстура, возвращающая список транзакций для тестирования"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    ]


def test_filter_by_currency(transactions: List[Dict[str, Any]]) -> None:
    """Тест функции фильтрации по валюте"""
    result_transaction = filter_by_currency(transactions, "USD")

    # Проверка первой транзакции
    first_transaction = next(result_transaction)
    assert first_transaction["operationAmount"]["currency"]["code"] == "USD"
    assert first_transaction["id"] == 939719570

    # Проверка второй транзакции
    second_transaction = next(result_transaction)
    assert second_transaction["operationAmount"]["currency"]["code"] == "USD"
    assert second_transaction["id"] == 142264268
