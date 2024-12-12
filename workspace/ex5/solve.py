from sage.all import *
from ecc import ECC


def main():
    ecc = ECC(curve_id=2)

    P = ecc.curve(33500, 33693)
    Q = ecc.curve(62753, 51897)

    # R1 = A1 * P + B1 * Q
    A1 = 68596
    B1 = 19260
    print(f"R1 = {A1 * P + B1 * Q}")

    # R2 = A2 * P + B2 * Q
    A2 = 63229
    B2 = 46711
    print(f"R2 = {A2 * P + B2 * Q}")

    # s = - ((A1 - A2) / (B1 - B2))
    A = Mod(A1 - A2, ecc.order)
    B = Mod(B1 - B2, ecc.order)
    print(f"s = {- A / B}")


if __name__ == "__main__":
    main()
