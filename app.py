from flask import Flask
from ticket_booking_app.routes import ticket_booking_app_bp


import sys

app = Flask(__name__)


app.register_blueprint(ticket_booking_app_bp)


if __name__ == '__main__':
    #DO not remove any Code below
    port = int(sys.argv[1])
    app.run(debug=True, host="0.0.0.0", port=port)
