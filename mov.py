import os


"""
Program: Movie List

"""


class Movie:

    def __init__(self, movie_name, movie_id="000", movie_genre="", movie_info="", movie_studio=""):
        self.id = movie_id
        self.name = movie_name
        # self.genre = movie_genre
        # self.info = movie_info
        # self.studio = movie_studio
        self.data = {
            'name': movie_name,
            'genre': movie_genre,
            'studio': movie_studio,
            'info': movie_info
        }

    def __str__(self):
        text = f"[{self.id}]\t {self.name}: {self.data}"
        return text

    def add_attr(self, attr_key, new_attr_value):
        valid_attr = [
            'name',
            'genre',
            'studio',
            'info'
        ]
        if attr_key in valid_attr:
            self.data[attr_key] = new_attr_value


class MovieList:
    ID_NUM = 0

    def __init__(self):
        self.movies = {}

    def __str__(self):
        text = ""
        for id, mov in self.movies.items():
            text += f"[{id}] \t {mov.name}\n"
        return text

    def print_movies(self):
        for id, mov in self.movies.items():
            print(f"[{id}] \t {mov.name}\n")

    def add_movie(self, name, genre="", info="", studio=""):
        self.ID_NUM += 1

        new_id = f"{self.ID_NUM:03}"
        new_movie = Movie(movie_name=name, movie_id=new_id, movie_genre=genre, movie_info=info, movie_studio=studio)
        # Does it matter if I use new_id vs. new_movie.id ????
        self.movies[new_id] = new_movie

    def update_movie(self, movie_id, attr_key, attr_value):
        movie = self.movies.get(movie_id)
        movie.add_attr(attr_key, attr_value)

    def get_id(self, movie_name):
        """
        Get Movie ID from Movie Name
        """
        for m_id, m_name in self.movies.items():
            if m_name.name == movie_name:
                return m_id
        return False

    def check_id(self, movie_id):
        check = self.movies.get(movie_id)
        if check is None:
            return False
        return True

    def search(self, movie_name="n/a", movie_id="000"):
        """
        """
        search_query = ""
        if movie_name != "n/a":
            search_query = self.get_id(movie_name)
        if movie_id != "000":
            search_query = movie_id

        return self.movies.get(search_query)

    def get_imbd(self, movie_id):
        """
        Use an api or database to get more info on a specific movie
        """
        pass


if __name__ == "__main__":
    my_movies = MovieList()

    my_movies.add_movie("Pokemon: Mewtwo strikes Back")
    current_id = my_movies.get_id("Pokemon: Mewtwo strikes Back")
    my_movies.update_movie(current_id, 'genre', 'adventure')
    print(my_movies.search("Pokemon: Mewtwo strikes Back"))

    my_movies.print_movies()
    print(my_movies)
