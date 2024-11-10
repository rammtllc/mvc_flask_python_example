from flask import Blueprint, render_template
from models import get_greeting

# Define a blueprint
main_controller = Blueprint(
    "main", __name__, static_folder="static"
)

@main_controller.route("/")
def index():
    """Controller for the index route."""
    greeting = get_greeting()
    return render_template("views/index.html", greeting=greeting)
