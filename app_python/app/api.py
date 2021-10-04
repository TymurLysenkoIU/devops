from flask import Blueprint, current_app
from prometheus_client import Counter  # type: ignore[import]
import datetime
from pathlib import Path
from logging import Logger
from typing import Optional

bp = Blueprint("api", __name__)

current_time_requests = Counter(  # type: ignore[no-any-unimported,misc]
    'current_time_requests', 'Number of requests made')


def _get_file_path() -> Optional[Path]:
    visits_file_path: str = current_app.config.get(
        'VISITS_FILE')  # type: ignore[assignment]
    if visits_file_path:
        return Path(visits_file_path)
    else:
        return None


@bp.route("/")  # type: ignore[misc]
def current_time() -> str:  # type: ignore[misc]
    now: datetime.datetime = datetime.datetime.now(datetime.timezone.utc)
    result: str = now.isoformat()

    logger: Logger = current_app.logger
    logger.info(f'Request current time. Responding with "{result}"')

    current_time_requests.inc()  # type: ignore[misc]

    if path := _get_file_path():
        try:
            contents = path.read_text()
            new_value: int = int(contents) + 1
        except Exception:
            new_value = 1

        path.write_text(f'{new_value}')

    return result


@bp.route("/visits")  # type: ignore[misc]
def num_visits() -> str:  # type: ignore[misc]
    try:
        path: Optional[Path] = _get_file_path()
        if path:
            result: int = int(path.read_text())
        else:
            result = 0
    except Exception:
        result = 0

    return f'{result}'
