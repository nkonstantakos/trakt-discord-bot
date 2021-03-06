from sqlite3 import Connection


def create_movie_table(connection):
    """
    @type connection: Connection
    """
    connection.execute('''CREATE TABLE IF NOT EXISTS MOVIES
                         (movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                         imdb_id TEXT,
                         movie_name TEXT,
                         creator INTEGER,
                         approved INTEGER,
                         declined INTEGER,
                         deleted INTEGER,
                         private INTEGER,
                         channel_id INTEGER,
                         trakt_id INTEGER,
                         FOREIGN KEY(creator) REFERENCES PLEX_USERS (user_id))''')
