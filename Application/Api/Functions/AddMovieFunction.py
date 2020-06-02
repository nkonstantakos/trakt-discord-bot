from Application.Dao.MovieBotDao import MovieBotDao
from Application.Domain.PlexUser import PlexUser
from Application.Domain.Movie import Movie


class AddMovieFunction(object):
    def __init__(self, config, dao):
        """
        @type config: configparser.ConfigParser
        @type dao: MovieBotDao
        """
        self.config = config
        self.dao = dao

    def add_movie(self, author, imdb_id, private):
        user_record: PlexUser = self.dao.get_user_by_discord_id(author)
        if user_record is None:
            new_user = PlexUser(None, author.id, author.name, False, False)
            user_record = self.dao.insert_user(new_user)

        approved: bool = user_record.admin or user_record.moderator
        new_movie: Movie = Movie(imdb_id=imdb_id, movie_name=None, creator=user_record.user_id, approved=approved, declined=False, deleted=False, private=private)
        self.dao.insert_movie(new_movie)