from dataclasses import dataclass


@dataclass
class AppConfig:
    """Flask application strongly-typed config"""
    TESTING: bool = False
