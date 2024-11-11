from flask import Blueprint, request, jsonify, render_template, abort
from models import get_greeting, generate_short_url

# URL storage class
class URLStorage:
    def __init__(self):
        self.url_map = {}

    def add_url(self, short_url, long_url):
        self.url_map[short_url] = long_url

    def get_url(self, short_url):
        return self.url_map.get(short_url)

# Create a global URL storage instance
url_storage = URLStorage()

# Define a blueprint for the app
main_controller = Blueprint("main", __name__, static_folder="static")

@main_controller.route("/")
def index():
    """Main route that shows a greeting message."""
    greeting = get_greeting()
    return render_template("views/index.html", greeting=greeting)

@main_controller.route("/urls")
def urls():
    """Shows the links page with a greeting."""
    greeting = get_greeting()
    return render_template("views/urls.html", greeting=greeting)

# API to shorten a URL
@main_controller.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()  # Use get_json() for cleaner JSON parsing
    long_url = data.get('url')

    if not long_url:
        abort(400, description="URL is required")

    short_url = generate_short_url(long_url)
    url_storage.add_url(short_url, long_url)

    return jsonify({'short_url': short_url, 'long_url': long_url})

# API to expand a short URL
@main_controller.route('/urls<short_url>', methods=['GET'])
def expand_url(short_url):
    """Expand a shortened URL to its original form."""
    long_url = url_storage.get_url(short_url)
    
    if not long_url:
        abort(404, description="URL not found")

    return jsonify({'long_url': long_url})

