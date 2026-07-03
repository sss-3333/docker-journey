## Flask Web Application:

#A Flask app that has two routes:
#/: Displays a welcome message.
#/count: Increments and displays a visit count stored in Redis.

## Flask Web Application with Redis

import os
from flask import Flask
import redis

app = Flask(__name__)
# Creating environment variables
redis_host = os.getenv('REDIS_HOST', 'redis')                    #retrieves redis host from environment variables
redis_port = int(os.getenv('REDIS_PORT', 6379))

# Create Redis connection once, reused across both routes
r = redis.Redis(host='redis', port=6379, db=0)

@app.route('/')
def welcome_message():
    return 'Welcome! Visit /count to see the visit counter.'

@app.route('/count')
def challenge_count():
    # INCR increments the value of a key by 1 each time it's called
    # If the key doesn't exist yet, Redis creates it and starts from 1
    count = r.incr('visit_count')
    return f'Number of times visited: {count}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
