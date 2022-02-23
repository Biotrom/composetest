import time
import os
import redis

from flask import Flask
from couchdbClass import MyCouchDB

app = Flask(__name__)
host_run=os.environ.get('HOST_RUN', '0.0.0.0')
debug=os.environ.get('DEBUG', 'True')

# def get_hit_count():
#     retries = 5
#     while True:
#         try:
#             return cache.incr('hits')
#         except redis.exceptions.ConnectionError as exc:
#             if retries == 0:
#                 raise exc
#             retries -= 1
#             time.sleep(0.5)

def get_tabelas():
    user = "admin"
    password = "123456789"
    couch = MyCouchDB(user, password)
    print(couch.getDatabases())
    # couch.getDocs("datasimportantes")
    

@app.route('/')
def hello():
    try:
        varivavel = os.environ["LOCAL_BANK"]
    except Exception as e:
        varivavel = e
    return 'Hello World!\nVariavel {}'.format(varivavel)

if __name__ == "__main__":
   app.run(host=host_run, debug=debug)