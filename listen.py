import select
from connection import get_connection


conn = get_connection()
cursor = conn.cursor()
cursor.execute("LISTEN CHANNEL_1;")

while True:
    select.select([conn], [], [])
    conn.poll()
    while conn.notifies:
        notify = conn.notifies.pop()
        print("Got NOTIFY: ", notify.pid, notify.channel, notify.payload)
