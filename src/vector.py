import math

class Vector:
    """Numerical vector in R^n with some operations.
    """
    def __init__(self, values=None):
        if values is None:
            values = []
        for value in values:
            if not isinstance(value, (int, float)):
                raise ValueError('Vector should be numerical, '
                                 f'{type(value).__name__} provided.')
        self._vector = values

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self._vector == other._vector
        else:
            return False

    def __getitem__(self, key):
        return self._vector[key]

    def __setitem__(self, key, value):
        if isinstance(value, (int, float)):
            self._vector[key] = value
        else:
            raise ValueError('Vector should be numerical, '
                             f'{type(value).__name__} provided.')

    def __len__(self):
        return len(self._vector)

    def __neg__(self):
        return Vector([-value for value in self])

    def __add__(self, other):
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError('Vectors should have same length to '
                                 'perform an operation.')
            return Vector([self[i] + other[i] for i in range(len(self))])
        elif isinstance(other, (int, float)):
            return Vector([value + other for value in self])
        else:
            raise ValueError('Input for the operation should be numerical, '
                             f'{type(other).__name__} provided.')

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if not isinstance(other, (Vector, int, float)):
            raise ValueError('Input for the operation should be numerical, '
                             f'{type(other).__name__} provided.')
        return self + (-other)

    def __rsub__(self, other):
        return -(self - other)

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise ValueError('Input for the operation should be a number, '
                             f'{type(other).__name__} provided.')
        return Vector([value * other for value in self])

    def __rmul__(self, other):
        return self * other

    def __matmul__(self, other):
        if not isinstance(other, Vector):
            raise ValueError('Input for the operation should be a vector, '
                             f'{type(other).__name__} provided.')
        if len(self) != len(other):
            raise ValueError('Vectors should have same length to '
                             'perform an operation.')
        return sum(Vector([self[i] * other[i] for i in range(len(self))]))

    def __str__(self):
        return str(self._vector)

    def norm(self):
        return math.sqrt(self @ self)
