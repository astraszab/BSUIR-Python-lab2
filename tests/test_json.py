from lab2_package.json_serializer import dumps
import pytest


def test_none():
    assert dumps(None) == 'null'


def test_number():
    assert dumps(123) == '123'


def test_string():
    assert dumps('string') == '"string"'


def test_bool():
    assert dumps(True) == 'true'


def test_list():
    assert dumps([1, 2, True, None]) == '[1, 2, true, null]'


def test_dict():
    assert dumps({1: 'a', 'abc': None}) == '{"1": "a", "abc": null}'


def test_nested_dict():
    assert dumps({5: {'a': 3}, 'b': {'c': 4}}) == \
        '{"5": {"a": 3}, "b": {"c": 4}}'


def test_wrong_type():
    with pytest.raises(TypeError):
        dumps(...)


def test_infinity():
    with pytest.raises(ValueError):
        dumps(float('inf'))


def test_nan():
    with pytest.raises(ValueError):
        dumps(float('nan'))
