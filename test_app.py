import pytest
from app import calculate_profit


def test_profit_is_positive():
    result = calculate_profit(10000, 8500)
    assert result == {"profit": 1500, "decision": "Positive"}


def test_break_even():
    result = calculate_profit(5000, 5000)
    assert result == {"profit": 0, "decision": "Break-even"}


def test_loss():
    result = calculate_profit(5000, 6000)
    assert result == {"profit": -1000, "decision": "Loss"}


def test_negative_revenue_is_rejected():
    with pytest.raises(ValueError):
        calculate_profit(-100, 50)