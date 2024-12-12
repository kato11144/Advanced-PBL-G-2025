import pymysql
from datetime import datetime
from sage.all import *
from ecc import ECC


class RhoMethod:
    def __init__(self, n, q, r, P, Q):
        self.n = n
        self.q = q
        self.r = r

        self.P = P
        self.Q = Q

        self.conn = pymysql.connect(
            host='localhost',
            user='attacker',
            password='0000',
            database='RhoMethod',
            autocommit=True
        )
        self.cursor = self.conn.cursor()
        self.setup_database()
        self.generate_precompute_table()

    def setup_database(self):
        """データベースを初期化する"""
        self.cursor.execute("DROP TABLE IF EXISTS point_table")
        self.cursor.execute("""
            CREATE TABLE point_table (
                X INT,
                A INT,
                B INT,
                DATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

    def find_then_set_data(self, X, A, B):
        """データベースを検索し、なければ追加する"""
        self.cursor.execute("SELECT * FROM point_table WHERE X = %s", (int(X)))
        result = self.cursor.fetchone()
        if result is None:
            self.cursor.execute("INSERT INTO point_table (X, A, B) VALUES (%s, %s, %s)", (int(X), int(A), int(B)))
            return False
        return True

    def generate_precompute_table(self):
        """事前計算テーブルを生成する"""
        self.table = []

        for i in range(self.n):
            A = ZZ.random_element(0, self.r)
            B = ZZ.random_element(0, self.r)
            R = A * self.P + B * self.Q
            self.table.append({"R": R, "A": A, "B": B})

    def random_walk(self):
        """ランダムウォークを実行する"""
        A = ZZ.random_element(0, self.r)
        B = ZZ.random_element(0, self.r)
        R = A * self.P + B * self.Q
        if R.is_zero():
            print("found zero")
            return
        self.find_then_set_data(R[0], A, B)

        while True:
            idx = int(R[0]) % self.n
            A = (A + self.table[idx]["A"]) % self.r
            B = (B + self.table[idx]["B"]) % self.r
            R = R + self.table[idx]["R"]
            if R.is_zero():
                print("found zero")
                return
            if self.find_then_set_data(R[0], A, B):
                print("found collision")
                print(f"(X,A,B)=({R[0]},{A},{B})")
                break

    def close(self):
        """データベース接続を閉じる"""
        self.conn.close()

def main():
    n = 16
    ecc = ECC(curve_id=2)
    P = ecc.curve(33500, 33693)
    Q = ecc.curve(62753, 51897)

    rho = RhoMethod(n=n, q=ecc.prime, r=ecc.order, P=P, Q=Q)
    rho.random_walk()
    rho.close()


if __name__ == "__main__":
    main()
