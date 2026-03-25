import re
from typing import Any, Dict, List


def process_bank_search(data: List[Dict[str, Any]], search: str) -> List[Dict[str, Any]]:
    """Фильтрует операции по строке в описании (регулярные выражения)."""

    pattern = re.compile(search, re.IGNORECASE)

    result: List[Dict[str, Any]] = []

    for item in data:
        description = item.get("description", "")
        if pattern.search(description):
            result.append(item)

    return result


def process_bank_operations(data: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """Считает количество операций по категориям."""

    result: Dict[str, int] = {category: 0 for category in categories}

    for item in data:
        description = item.get("description", "")

        for category in categories:
            if category.lower() in description.lower():
                result[category] += 1

    return result
