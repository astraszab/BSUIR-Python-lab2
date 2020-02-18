from lab2_package.singleton import singleton


@singleton
class SampleClass:
    pass


def test_creates_single_object():
    instance1 = SampleClass()
    instance2 = SampleClass()
    assert instance1 is instance2
