from flask import Blueprint, jsonify
from ticket_booking_app.service import add_user
import sys
print(sys.path)

from ticket_booking_app.service import add_users,get_user,post_details,get_movie_details,book_tickets


ticket_booking_app_bp = Blueprint('ticket_booking_app', __name__)

@ticket_booking_app_bp.route("/addUsers", methods=["POST"])
def add_user_func():
    user = add_user()
    return jsonify(user)

@ticket_booking_app_bp.route("/getUser", methods=["GET"])
def get_user_func():
    user = get_user()
    return jsonify(user)

@ticket_booking_app_bp.route("/addMovie", methods=["POST"])
def post_details_func():
    movie =post_details()
    return jsonify(movie)

@ticket_booking_app_bp.route("/getMovie", methods=["GET"])
def get_movie_details_func():
    movie = get_movie_details()
    return jsonify(movie)

@ticket_booking_app_bp.route("/book/:movieId/numberOfTickets", methods=["POST"])
def book_tickets_func(movieId):
    movie_ticket =book_tickets(movieId)
    return jsonify(movie_ticket)
