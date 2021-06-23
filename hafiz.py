from flask import app
from hafiz.app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()