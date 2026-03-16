from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[..., Any]:  # декоратор с параметрами, основная функция-декоратор
    """
    Декоратор для логирования функций.

    :param filename: имя файла для записи логов; если None, вывод в консоль
    :return: декорированная функция
    """

    def decorator(
        func: Callable[..., Any],
    ) -> Callable[..., Any]:  # Функция, которая принимает int и str, возвращает bool
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Вспомогательная функция для записи логов
            def write_log(message: str) -> None:

                # Если указан файл - записываем лог в файл
                if filename:
                    # Открываем файл в режиме добавления ("a")
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")

                # Если файл не указан — выводим лог в консоль
                else:
                    print(message)

            try:
                # Пытаемся выполнить исходную функцию
                result: Any = func(*args, **kwargs)

                # Если функция выполнилась успешно — логируем это
                write_log(f"{func.__name__} ok")  # file.__name__ - имя функции

                # Возвращаем результат функции
                return result

            except Exception as e:
                # Если произошла ошибка — записываем её тип
                # и входные параметры функции
                write_log(
                    f"{func.__name__} error: {type(e).__name__}. "  # type(e).__name__ - имя ошибки
                    f"Inputs: {args}, {kwargs}"
                )

                # Повторно выбрасываем исключение,
                # чтобы программа знала, что произошла ошибка
                raise

                # Возвращаем обёртку функции

        return wrapper

        # Возвращаем сам декоратор

    return decorator
