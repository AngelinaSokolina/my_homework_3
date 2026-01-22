from typing import Any, Generator


def filter_by_currency(transactions: Any ,currency_code: Any) -> Generator[Any, Any, None]:
    for transaction in transactions:
        transaction_code = transaction["operationAmount"]["currency"]["code"]
        if transaction_code == currency_code:
            yield transaction
