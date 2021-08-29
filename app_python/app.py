from flask import Flask

import datetime

app = Flask(__name__)

@app.route("/")
def current_time():
    now: datetime.datetime = datetime.datetime.now(datetime.timezone.utc)
    return now.isoformat()
