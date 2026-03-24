from unittest.mock import patch

import pandas as pd

from src.data_loader import load_transactions_from_csv, load_transactions_from_xlsx

# CSV


@patch("pandas.read_csv")
def test_load_csv(mock_read_csv):
    # Мокаем возвращаемый DataFrame
    mock_read_csv.return_value = pd.DataFrame([{"id": 1}, {"id": 2}])

    result = load_transactions_from_csv("fake_path.csv")
    assert result == [{"id": 1}, {"id": 2}]
    mock_read_csv.assert_called_once_with("fake_path.csv")


@patch("pandas.read_csv")
def test_load_csv_empty(mock_read_csv):
    mock_read_csv.return_value = pd.DataFrame()
    result = load_transactions_from_csv("empty.csv")
    assert result == []


@patch("pandas.read_csv")
def test_load_csv_not_found(mock_read_csv):
    mock_read_csv.side_effect = FileNotFoundError
    result = load_transactions_from_csv("no_file.csv")
    assert result == []


# XLSX
@patch("pandas.read_excel")
def test_load_xlsx(mock_read_excel):
    mock_read_excel.return_value = pd.DataFrame([{"id": 1}, {"id": 2}])
    result = load_transactions_from_xlsx("fake.xlsx")
    assert result == [{"id": 1}, {"id": 2}]
    mock_read_excel.assert_called_once_with("fake.xlsx")


@patch("pandas.read_excel")
def test_load_xlsx_not_found(mock_read_excel):
    mock_read_excel.side_effect = FileNotFoundError
    result = load_transactions_from_xlsx("no_file.xlsx")
    assert result == []
