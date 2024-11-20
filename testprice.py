import pytest
import unittest
from price_info import total_cost_shopping , cost_of_fruits

def test_total_cost_shopping():
    expected_value = 46.75
    actual_value = total_cost_shopping()
    assert expected_value == actual_value

def test_cost_of_fruit():
    expected_value = 12
    actual_value = cost_of_fruits('apple', 10)
    assert expected_value==actual_value
