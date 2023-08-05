import psycopg2
import psycopg2.extensions


def get_connection():
    conn = psycopg2.connect(database='python4real',
                            user='postgres', password='1234', host='localhost')

    conn.set_isolation_level(
        psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
    )

    return conn
