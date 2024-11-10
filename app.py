from flask import Flask
from controllers import main_controller

app = Flask(__name__)

# Register blueprints (controllers)
app.register_blueprint(main_controller)

if __name__ == "__main__":
    app.run(debug=True)
