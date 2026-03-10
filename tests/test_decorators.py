import pytest

from src.decorators import log


# Тестирование вывода в консоль
def test_success_console(capsys):
    """
    Проверка успешного выполнения функции с логированием в консоль.
    capsys — фикстура pytest для перехвата вывода в stdout/stderr.
    """

    @log()  # без filename - вывод в консоль
    def add(a, b):
        return a + b

    result = add(2, 3)  # Вызов функции, результат должен быть 5
    console_output = capsys.readouterr().out  # текст, который был выведен в stdout

    assert result == 5  # Проверяем, что функция вернула правильный результат
    assert "add ok" in console_output  # Проверяем, что лог содержит сообщение об успешном выполнении


def test_exception_console(capsys):
    """
    Проверка обработки исключений с логированием в консоль.
    """

    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    console_output = capsys.readouterr().out
    assert "divide error" in console_output  # Проверяем, что лог содержит
    assert "ZeroDivisionError" in console_output
    assert "(1, 0)" in console_output


# Тестирование логирования в файл
def test_success_file(tmp_path):
    """
    Проверка успешного выполнения функции с логированием в файл.
    tmp_path — временная директория, создаваемая pytest.
    """
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def multiply(a, b):
        return a * b

    result = multiply(3, 4)
    assert result == 12
    # Считываем содержимое файла для проверки логов
    file_content = log_file.read_text(encoding="utf-8")
    assert "multiply ok" in file_content


def test_exception_file(tmp_path):
    """
    Проверка обработки исключений с логированием в файл.
    """
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def divide(a, b):
        return a / b

    # Проверяем, что функция выбрасывает ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

    file_content = log_file.read_text(encoding="utf-8")
    assert "divide error" in file_content
    assert "ZeroDivisionError" in file_content
    assert "(5, 0)" in file_content
