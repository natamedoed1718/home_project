import pandas as pd

from src.data_loader import load_transactions_from_csv, load_transactions_from_xlsx


# csv
def test_load_csv(tmp_path):
    file = tmp_path / "test.csv"

    df = pd.DataFrame([{"id": 1}, {"id": 2}])
    df.to_csv(file, index=False)

    result = load_transactions_from_csv(str(file))
    assert result == [{"id": 1}, {"id": 2}]


def test_load_csv_empty(tmp_path):
    file = tmp_path / "empty.csv"
    file.write_text("")

    result = load_transactions_from_csv(str(file))
    assert result == []


def test_load_csv_not_found():
    result = load_transactions_from_csv("no_file.csv")
    assert result == []


# XLSX


def test_load_xlsx(tmp_path):
    file = tmp_path / "test.xlsx"

    df = pd.DataFrame([{"id": 1}, {"id": 2}])
    df.to_excel(file, index=False)

    result = load_transactions_from_xlsx(str(file))
    assert result == [{"id": 1}, {"id": 2}]


def test_load_xlsx_not_found():
    result = load_transactions_from_xlsx("no_file.xlsx")
    assert result == []
