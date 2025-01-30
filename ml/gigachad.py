from dataclasses import dataclass


@dataclass
class Expense:
    fuel: str = 0.0
    maintenance: str = 0.0
    other: str = 0.0
    total: str = 0.0
    overall_analysis: str = ""


def test_ai(model: str, age: int, mileage: float, context: str) -> Expense:
    return Expense(
        fuel="1",
        maintenance="1",
        other="1",
        total="1",
        overall_analysis="1",
    )
