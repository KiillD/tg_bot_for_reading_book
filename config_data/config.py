from dataclasses import dataclass
from environs import Env


@dataclass
class Tg_Bot:
    token: str
    admin_ids: list[int]


@dataclass
class Config:
    tg_bot: Tg_Bot


def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)
    return Config(tg_bot=Tg_Bot(
        token=env('BOT_TOKEN'),
        admin_ids=env('ADMIN_IDS')))
