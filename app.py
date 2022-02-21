from nis import cat
import time
import os

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
host_run=os.environ.get('HOST_RUN', '0.0.0.0')
debug=os.environ.get('DEBUG', 'True')

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    try:
        varivavel = os.environ["LOCAL_BANK"]
    except Exception as e:
        varivavel = e
    return 'Hello World! I have been seen {} times.\nVariavel {}'.format(count, varivavel)

if __name__ == "__main__":
   app.run(host=host_run, debug=debug)