import pytest
from myfile import find_largest, find_smallest

def test_find_largest_simple():
    numbers = [1, 2, 3, 4, 5]
    assert find_largest(numbers) == 5

def test_find_largest_complex():
    numbers = [-10, -20, -3, -5]
    assert find_largest(numbers) == -3

def test_find_smallest_simple():
    numbers = [1, 2, 3, 4, 5]
    assert find_smallest(numbers) == 1

def test_find_smallest_complex():
    numbers = [-10, -20, -3, -5]
    assert find_smallest(numbers) == -20

if __name__ == "__main__":
    pytest.main()