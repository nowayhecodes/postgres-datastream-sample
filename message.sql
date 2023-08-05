CREATE TABLE message(
    id SERIAL PRIMARY KEY,
    channel INTEGER NOT NULL,
    source TEXT NOT NULL,
    content TEXT NOT NULL
);

INSERT INTO message(channel, source, content)
    VALUES(1, 'gus', 'hello');