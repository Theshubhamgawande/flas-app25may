from flask import Flask
import redis
import os

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
r = redis.Redis(host=redis_host, port=6379)

@app.route('/')
def index():
    r.incr('hits')
    count = r.get('hits').decode('utf-8')
    return f'Hello! This page has been visited {count} times.'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)



