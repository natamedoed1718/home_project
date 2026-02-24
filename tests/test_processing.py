import pytest
from src.processing import filter_by_state,sort_by_date

@pytest.mark.parametrize(
    "state, expected_len",
    [
        ("EXECUTED", 2),
        ("CANCELED", 2),
        ("PENDING", 0),
    ],
)
def test_filter_by_state(operations, state, expected_len):
    # Вызываем функцию фильтрации
    result = filter_by_state(operations, state)
    assert len(result) == expected_len

@pytest.mark.parametrize(
    "reverse, expected_order",
    [
        (
            True,
            [
                "2019-07-03T18:35:29",
                "2018-10-14T08:21:33",
                "2018-09-12T21:27:25",
                "2018-06-30T02:08:58",
            ],
        ),
        (
            False,
            [
                "2018-06-30T02:08:58",
                "2018-09-12T21:27:25",
                "2018-10-14T08:21:33",
                "2019-07-03T18:35:29",
            ],
        ),
    ],
)
def test_sort_by_date_full_order(operations, reverse, expected_order):
    result = sort_by_date(operations, reverse=reverse)

    # сравниваем без микросекунд
    assert [item["date"][:19] for item in result] == expected_order

# одинаковые даты
def test_sort_by_date_same_dates():
    data = [
        {"date": "2024-01-01"},
        {"date": "2024-01-01"},
    ]

    result = sort_by_date(data)

    assert len(result) == 2

 # нестандартный формат
def test_sort_by_date_invalid_format():
    data = [
        {"date": "Некорректная дата"},
        {"date": "2024-01-01"},
    ]

    result = sort_by_date(data)

    assert len(result) == 2



