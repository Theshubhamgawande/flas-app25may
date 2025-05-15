import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return f"Hello from {os.getenv('APP_NAME', 'DefaultApp')} running on {os.getenv('ENV', 'development')} environment!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

