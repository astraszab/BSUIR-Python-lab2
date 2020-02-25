from lab2.src.json_serializer import dumps
import json
import pytest


def test_none():
    assert dumps(None) == json.dumps(None)


def test_number():
    assert dumps(123) == json.dumps(123)


def test_string():
    assert dumps('string') == json.dumps('string')


def test_bool():
    assert dumps(True) == json.dumps(True)


def test_list():
    assert dumps([1, 2, True, None]) == json.dumps([1, 2, True, None])


def test_dict():
    assert dumps({1: 'a', 'abc': None}) == json.dumps({1: 'a', 'abc': None})


def test_nested_dict():
    obj = {5: {'a': 3},
           'b': {'c': {3: 5}},
           True: False,
           None: [1, 2, 3, 4, 5],}
    assert dumps(obj) == \
        json.dumps(obj)


def test_wrong_type():
    with pytest.raises(TypeError):
        dumps(...)


def test_infinity():
    with pytest.raises(ValueError):
        dumps(float('inf'))


def test_nan():
    with pytest.raises(ValueError):
        dumps(float('nan'))
