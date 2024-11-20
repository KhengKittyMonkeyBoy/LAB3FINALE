import employee_info
from employee_info import get_employees_by_age_range, calculate_average_salary, get_employees_by_dept
import pytest, unittest

def test_get_employees_by_age_range():
    expected_result = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    ]
    result = get_employees_by_age_range(22,31)
    assert result == expected_result

def test_average_salary():
    expected_result = 60166.666666666664
    actual_result = calculate_average_salary()
    assert expected_result == actual_result


