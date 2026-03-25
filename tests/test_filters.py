from src.filters import process_bank_operations, process_bank_search


def test_search_found():
    data = [
        {"description": "Перевод с карты"},
        {"description": "Открытие вклада"},
    ]

    result = process_bank_search(data, "перевод")

    assert result == [{"description": "Перевод с карты"}]


def test_search_case_insensitive():
    data = [
        {"description": "Перевод с карты"},
    ]

    result = process_bank_search(data, "ПЕРЕВОД")

    assert len(result) == 1


def test_search_not_found():
    data = [
        {"description": "Открытие вклада"},
    ]

    result = process_bank_search(data, "перевод")

    assert result == []


def test_search_empty_data():
    result = process_bank_search([], "перевод")
    assert result == []


def test_operations_count():
    data = [
        {"description": "Перевод с карты"},
        {"description": "Перевод на счет"},
        {"description": "Открытие вклада"},
    ]

    categories = ["Перевод", "Открытие"]

    result = process_bank_operations(data, categories)

    assert result == {
        "Перевод": 2,
        "Открытие": 1,
    }


def test_operations_no_matches():
    data = [
        {"description": "Открытие вклада"},
    ]

    categories = ["Перевод"]

    result = process_bank_operations(data, categories)

    assert result == {"Перевод": 0}


def test_operations_empty_data():
    result = process_bank_operations([], ["Перевод"])

    assert result == {"Перевод": 0}
