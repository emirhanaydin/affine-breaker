class Affine:
    def __init__(self, m: int, a: int, b: int):
        self.m = m
        self.a = a
        self.b = b

    def decode(self, x: int):
        m = self.m
        a = self.a
        b = self.b
        return int((pow(a, -1, m) * (x - b)) % m)


class AffineBuilder:
    def __init__(self, m: int):
        self._m = m

    def build_affine(self, d1: int, e1: int, d2: int, e2: int):
        m = self._m
        inv_c_a = pow(d1 - d2, -1, m)
        a = (inv_c_a * (e1 - e2)) % m
        b = (e1 - (a * d1)) % m

        return Affine(m, a, b)
