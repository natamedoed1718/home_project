import json
from src.utils import load_transactions


# Файл с корректным списком
def test_load_transactions_valid(tmp_path):
    # Создаём временный JSON-файл со списком транзакций
    data = [{"id": 1}, {"id": 2}]
    file = tmp_path / "transactions.json"  # tmp_path временный файл
    file.write_text(json.dumps(data))

    result = load_transactions(str(file))
    assert result == data


# Файл пустой


def test_load_transactions_empty(tmp_path):
    file = tmp_path / "transactions.json"
    file.write_text("")  # пустой файл

    result = load_transactions(str(file))
    assert result == []


# Файл содержит не список


def test_load_transactions_not_list(tmp_path):
    file = tmp_path / "transactions.json"
    file.write_text(json.dumps({"id": 1}))  # словарь, а не список

    result = load_transactions(str(file))
    assert result == []


#  Файл не существует


def test_load_transactions_file_not_found():
    result = load_transactions("missing_file.json")
    assert result == []
