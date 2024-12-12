from sage.all import *

CURVES = {
    1: {"prime": 2143,      "order": 2089,      "a": 0, "b": 5},
    2: {"prime": 75223,     "order": 74929,     "a": 0, "b": 7},
    3: {"prime": 1706311,   "order": 1704961,   "a": 0, "b": 3},
    4: {"prime": 99286339,  "order": 99276253,  "a": 0, "b": 3},
    5: {"prime": 258220873, "order": 258204649, "a": 0, "b": 10},
    6: {"prime": 323505271, "order": 323487121, "a": 0, "b": 3},
}


class ECC:
    def __init__(self, curve_id):
        curve = CURVES[curve_id]
        self.prime = curve["prime"]
        self.order = curve["order"]
        self.a = curve["a"]
        self.b = curve["b"]
        self.field = GF(self.prime)
        self.curve = EllipticCurve(self.field, [self.a, self.b])

    def random_point(self):
        """ランダムな点を生成する"""
        while True:
            R = self.curve.random_element()
            if not R.is_zero():
                return R

    def problem(self):
        """問題を生成する"""
        P = self.random_point()
        s = ZZ.random_element(1, self.order)
        Q = s * P
        return P, Q, s

def main():
    ecc = ECC(curve_id=2)
    P, Q, s = ecc.problem()

    print("P =", P)
    print("Q =", Q)
    print("s =", s)


if __name__ == "__main__":
    main()
