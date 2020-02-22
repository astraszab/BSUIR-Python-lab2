import pytest
from lab2.src.cached import cached
from time import time


def fibonacci(n, **kwargs):
    if n == 1 or n == 0:
        return 1
    else:
        return fibonacci(n - 1, **kwargs) + fibonacci(n - 2, **kwargs)


def test_function_returns_same_output():
    assert fibonacci(10) == cached(fibonacci)(10)


def test_function_returns_same_output_for_kwargs():
    assert fibonacci(n=10) == cached(fibonacci)(n=10)


def test_cached_works_faster():
    start = time()
    fibonacci(32)
    usual_time = time() - start
    start = time()
    cached(fibonacci)(32)
    cached_time = time() - start
    assert cached_time < usual_time


def test_warning_if_unhashable_args():
    with pytest.warns(RuntimeWarning):
        res = cached(fibonacci)(10, unhashable=[1, 2, 3])
        assert res == fibonacci(10, unhashable=[1, 2, 3])
