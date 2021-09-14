from flask import Blueprint, current_app
from prometheus_client import Counter
import datetime
from logging import Logger

bp = Blueprint("api", __name__)

current_time_requests = Counter('current_time_requests', 'Number of requests made')

@bp.route("/")  # type: ignore[misc]
def current_time() -> str:  # type: ignore[misc]
    now: datetime.datetime = datetime.datetime.now(datetime.timezone.utc)
    result: str = now.isoformat()

    logger: Logger = current_app.logger
    logger.info(f'Request current time. Responding with "{result}"')

    current_time_requests.inc()

    return result
