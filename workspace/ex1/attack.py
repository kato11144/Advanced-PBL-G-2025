import pymysql
from datetime import datetime
from sage.all import *


class RhoMethod:
    def __init__(self, q, r):
        self.q = q
        self.r = r

        self.conn = pymysql.connect(
            host='localhost',
            user='attacker',
            password='0000',
            database='RhoMethod',
            autocommit=True
        )
        self.cursor = self.conn.cursor()
        self.setup_database()

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

    def random_walk(self):
        """ランダムウォークを実行する"""
        while True:
            A = ZZ.random_element(0, self.r)
            B = ZZ.random_element(0, self.r)
            X = ZZ.random_element(0, self.q)
            if self.find_then_set_data(X, A, B):
                print("found collision")
                print(f"(X,A,B)=({X},{A},{B})")
                break

    def close(self):
        """データベース接続を閉じる"""
        self.conn.close()

def main():
    q = 75223
    r = 74929
    rho = RhoMethod(q=q, r=r)
    rho.random_walk()
    rho.close()


if __name__ == "__main__":
    main()
