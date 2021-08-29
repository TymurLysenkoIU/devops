from flask import Blueprint
import datetime

bp = Blueprint("api", __name__)


@bp.route("/")
def current_time() -> str:
    now: datetime.datetime = datetime.datetime.now(datetime.timezone.utc)
    return now.isoformat()
