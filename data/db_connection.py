import sqlite3


def connect_db(file_name: str):
    connection = sqlite3.connect(f".\\data\\{file_name}")
    connection.row_factory = sqlite3.Row
    return connection


connection = connect_db("answers.db")


async def create_table(db: sqlite3.Connection):
    cursor = db.cursor()
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS answers
                (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(256),
                doc_1 INTEGER,
                doc_2 INTEGER,
                doc_3 INTEGER
                )
                """
    ) 
    db.commit()
    cursor.close()


async def get_image(doc: int):
    doctor = f"doc_{doc}"
    cursor = connection.cursor()
    query = cursor.execute(f"SELECT * FROM answers WHERE {doctor} IS NULL").fetchone()
    if query is not None:
        query = dict(query)
    else:
        query = {}
        query["name"] = "eof"
    cursor.close()
    return query


async def insert_stage_to_db(id: int, doc: int, stage: int):
    cursor = connection.cursor()
    doctor = f"doc_{doc}"
    # SQL инъекция мб, но не знаю как это пофиксить
    cursor.execute(f"UPDATE answers SET {doctor} = ? WHERE id = ?", (stage,id))
    connection.commit()