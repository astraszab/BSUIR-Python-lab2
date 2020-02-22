from lab2.src.singleton import singleton


@singleton
class SampleClass:
    pass


def test_creates_single_object():
    instance1 = SampleClass()
    instance2 = SampleClass()
    assert instance1 is instance2
