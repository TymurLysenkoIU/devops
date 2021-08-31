from flask import Blueprint
import datetime

bp = Blueprint("api", __name__)


@bp.route("/")  # type: ignore[misc]
def current_time() -> str:  # type: ignore[misc]
    now: datetime.datetime = datetime.datetime.now(datetime.timezone.utc)
    return now.isoformat()
