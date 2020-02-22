from lab2.src.external_sort import external_sort
from tempfile import TemporaryDirectory
from os.path import join
import pytest


@pytest.fixture
def tempdir():
    dir = TemporaryDirectory()
    return dir


def get_result(input_array, number_of_blocks, tempdir):
    with open(join(tempdir.name, 'input.txt'), 'w') as file:
        file.write(' '.join(str(value) for value in input_array))
    external_sort(
        join(tempdir.name, 'input.txt'),
        number_of_blocks,
        join(tempdir.name, 'output.txt'))
    with open(join(tempdir.name, 'output.txt'), 'r') as file:
        result = file.read()
    return result


def test_empty_input(tempdir):
    assert get_result([], 10, tempdir) == ''


def test_short_input(tempdir):
    assert get_result([5, 4, -10, 2, 3, 11, 8, 0, 3, 11], 3, tempdir) == \
        '-10 0 2 3 3 4 5 8 11 11'


def test_big_block(tempdir):
    assert get_result([5, 4, -10, 2, 3, 11, 8, 0, 3, 11], 20, tempdir) == \
        '-10 0 2 3 3 4 5 8 11 11'


def test_negative_block_size(tempdir):
    with pytest.raises(ValueError):
        get_result([3, 4, 1], -4, tempdir)


def test_not_integers(tempdir):
    with pytest.raises(ValueError):
        get_result(['a', 'b', 'c'], 3, tempdir)
