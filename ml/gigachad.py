from dataclasses import dataclass


@dataclass
class Expense:
    fuel: str = "0.0"
    maintenance: str = "0.0"
    other: str = "0.0"
    total: str = "0.0"
    overall_analysis: str = "0.0"


def test_ai(model: str, age: int, mileage: float, context: str) -> Expense:
    res = Expense()

    return res
