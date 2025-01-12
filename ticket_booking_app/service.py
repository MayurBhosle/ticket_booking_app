from database import get_db_connection

def add_user():
    user={"name":"test"}
    return user

def get_user():
    user=[{"name":"test"}]
    return user


def post_details():
    movie={"name":"test"}
    return movie


def get_movie_details():
    movie=[{"name":"test"}]
    return movie

def book_tickets(movieId):
    movie_ticket=[{"name":"test"}]
    return movie_ticket