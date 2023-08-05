CREATE OR REPLACE FUNCTION notify_on_insert() RETURNS TRIGGER LANGUAGE PLPGSQL AS $$ BEGIN PERFORM pg_notify('channel_' || NEW.channel, CAST(row_to_json(NEW) AS TEXT)); RETURN NULL; END;
$$;

CREATE TRIGGER notify_on_message_insert AFTER INSERT ON message FOR EACH ROW EXECUTE PROCEDURE notify_on_insert();

LISTEN CHANNEL_1;