def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""

    # Очищаем строку от возможных пробелов (на всякий случай)
    card_number = card_number.strip()

    # Проверяем условия, потому что недоверяем вводу пользователя
    if not card_number.isdigit() or len(card_number) != 16:
        return "Ошибка: номер карты должен состоять из 16 цифр"

    # Если всё ок, маскируем
    mask_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

    return mask_card


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""

    # Очистка от пробелов
    account_number = account_number.strip()

    # Проверяем условия ввода пользователя
    if not account_number.isdigit() or len(account_number) != 20:
        return "Ошибка: номер счета должен состоять из 20 цифр"

    # Если всё ок, маскируем
    mask_account = f"**{account_number[-4:]}"

    return mask_account
