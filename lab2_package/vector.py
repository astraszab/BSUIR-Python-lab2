class Vector:
    def __init__(self, values):
        for value in values:
            if not isinstance(value, (int, float)):
                raise ValueError('Vector should be numerical, '
                                 f'{type(value).__name__} provided.')
        self._vector = values

    def __eq__(self, other):
        return self._vector == other._vector

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
            return Vector([self[i] + other[i] for i in range(len(self))])
        elif isinstance(other, (int, float)):
            return Vector([value + other for value in self])

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return Vector([value * other for value in self])

    def __matmul__(self, other):
        if len(self) != len(other):
            raise ValueError('Vectors should have same length to '
                             'perform an operation.')
        return sum(Vector([self[i] * other[i] for i in range(len(self))]))

    def __str__(self):
        return str(self._vector)
