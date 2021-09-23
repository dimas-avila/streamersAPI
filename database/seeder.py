import sqlite3 as sql


DB_PATH = "C:\\Users\\lokix\\OneDrive\\Documents\\yotube\\src\\streamersAPI\\database\\streamers.db"


def createDB():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE streamers (
        name text,
        subs integer,
        followers integer
    )""")
    conn.commit()
    conn.close()


def addValues():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    data = [
        ("alexelcapo", 10000, 800000),
        ("ibai", 25000, 7000000),
        ("elxokas", 10000, 1000000),
        ("auronplay", 20000, 8000000),
        ("cristinini", 5500, 3000000)
    ]
    cursor.executemany("""INSERT INTO streamers VALUES (?, ?, ?)""", data)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    createDB()
    addValues()
