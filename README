# postgres-datastream-sample 

This repo shows a sample on how to perform data streaming with PostgreSQL.

Create a trigger function using the `pg_notify()` function. 
Them create another trigger to call the first one everytime an insertion on the messages table occurs.

Using the PostgreSQL `LISTEN` function in the psql terminal we can get an output like this: 

![](https://github.com/nowayhecodes/postgres-datastream-sample/blob/main/screens/psql.png "psql screenshot")

Then running the `listen.py` file: 

![](https://github.com/nowayhecodes/postgres-datastream-sample/blob/main/screens/terminal.png "terminal screenshot")

And then, running the `main.py` file (which is a flask app) in another terminal, then calling `http://127.0.0.1/message/1` on Postman: 

![](https://github.com/nowayhecodes/postgres-datastream-sample/blob/main/screens/postman.png "postman screenshot")

This way we can do SSE to our frontends, or other integrations with message queues and stuff. 
