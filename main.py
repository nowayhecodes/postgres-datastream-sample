from flask import Flask, Response
import select

from connection import get_connection

app = Flask(__name__)


def stream_messages(channel):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("LISTEN CHANNEL_{};".format(int(channel)))

    while True:
        select.select([conn], [], [])
        conn.poll()
        while conn.notifies:
            notify = conn.notifies.pop()
            yield f"data: {notify.payload}\n\n"


@app.route("/message/<channel>", methods=["GET"])
def get_messages(channel):
    return Response(stream_messages(channel), mimetype='text/event-stream')


if __name__ == "__main__":
    app.run()
