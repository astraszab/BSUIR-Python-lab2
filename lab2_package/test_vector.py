from lab2_package.vector import Vector
import pytest


def test_equality():
    v1 = Vector([1, 2, 3])
    v2 = Vector([1, 2, 3])
    assert v1 == v2


def test_vector_sum():
    v1 = Vector([1, 2, 3, 4])
    v2 = Vector([3, 2, 4, 1])
    assert v1 + v2 == Vector([4, 4, 7, 5])


def test_vector_difference():
    v1 = Vector([1, 2, 3, 4])
    v2 = Vector([3, 2, 4, 1])
    assert v1 - v2 == Vector([-2, 0, -1, 3])


def test_scalar_sum():
    v = Vector([1, 2, 3, 4, 5])
    assert v + 1 == Vector([2, 3, 4, 5, 6])


def test_scalar_difference():
    v = Vector([1, 2, 3, 4, 5])
    assert v - 1 == Vector([0, 1, 2, 3, 4])


def test_product():
    v = Vector([1, 2, 3])
    assert v * 3 == Vector([3, 6, 9])


def test_dot_product():
    v1 = Vector([2, 3, 4])
    v2 = Vector([-2, 1, -3])
    assert v1 @ v2 == -13


def test_length():
    v = Vector([1, 2, 3, 4, 5])
    assert len(v) == 5


def test_index_access():
    v = Vector([4, 3, 0, 2, -1])
    assert v[3] == 2


def test_index_modification():
    v = Vector([4, 3, 0, 2, -1])
    v[3] = 5
    assert v[3] == 5


def test_string_representation():
    v = Vector([3, 2, 1])
    assert str(v) == '[3, 2, 1]'


def test_index_error():
    v = Vector([1, 2, 3])
    with pytest.raises(IndexError):
        v[10]


def test_not_number():
    with pytest.raises(ValueError):
        Vector([1, 2, 'a'])


def test_modification_with_wrong_value():
    v = Vector([1, 2, 3])
    with pytest.raises(ValueError):
        v[1] = 'abc'


def test_different_lengths_for_dot_product():
    v1 = Vector([1, 2, 3, 4])
    v2 = Vector([1, 2, 3])
    with pytest.raises(ValueError):
        v1 @ v2
