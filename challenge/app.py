## Flask Web Application:

#A Flask app that has two routes:
#/: Displays a welcome message.
#/count: Increments and displays a visit count stored in Redis.

## Flask Web Application with Redis

import os
from flask import Flask, render_template_string
import redis

app = Flask(__name__)
# Creating environment variables
redis_host = os.getenv('REDIS_HOST', 'redis')                    #retrieves redis host from environment variables
redis_port = int(os.getenv('REDIS_PORT', 6379))

# Create Redis connection once, reused across both routes
r = redis.Redis(host='redis', port=6379, db=0)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Velvet Count</title>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background-color: #1a0010;
            color: #f2c4d0;
            font-family: 'Cormorant Garamond', serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            text-align: center;
        }
        h1 {
            font-size: 4rem;
            font-weight: 300;
            letter-spacing: 0.3em;
            color: #ff6b9d;
            margin-bottom: 0.5rem;
        }
        p {
            font-size: 1.2rem;
            font-weight: 300;
            letter-spacing: 0.15em;
            color: #c27b8f;
            margin-bottom: 3rem;
        }
        .count-box {
            border: 1px solid #ff6b9d44;
            padding: 2rem 4rem;
            margin-bottom: 2rem;
        }
        .count-number {
            font-size: 5rem;
            font-weight: 600;
            color: #ff6b9d;
            line-height: 1;
        }
        .count-label {
            font-size: 0.9rem;
            letter-spacing: 0.3em;
            color: #c27b8f;
            margin-top: 0.5rem;
            text-transform: uppercase;
        }
        a {
            color: #ff6b9d;
            text-decoration: none;
            letter-spacing: 0.2em;
            font-size: 0.9rem;
            text-transform: uppercase;
            border-bottom: 1px solid #ff6b9d44;
            padding-bottom: 2px;
            transition: border-color 0.3s;
        }
        a:hover { border-color: #ff6b9d; }
    </style>
</head>
<body>
    <h1>Velvet Count</h1>
    <p>an exercise in presence</p>
    {% if count is not none %}
        <div class="count-box">
            <div class="count-number">{{ count }}</div>
            <div class="count-label">visits recorded</div>
        </div>
        <a href="/">return</a>
    {% else %}
        <a href="/count">begin counting</a>
    {% endif %}
</body>
</html>
"""

@app.route('/')
def welcome_message():
    return render_template_string(HTML, count=None)

@app.route('/count')
def challenge_count():
    # INCR increments the value of a key by 1 each time it's called
    # If the key doesn't exist yet, Redis creates it and starts from 1
    count = r.incr('visit_count')
    return render_template_string(HTML, count=count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
