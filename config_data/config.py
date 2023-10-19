#config_data - дериктория с модулем конфигурации бота
#config_data.py - модулья для конфигурации бота

from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str #Токен для доступа к телеграм-боту
    admin_ids: list[int] #список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot


#создаем функцию, которая будет читать файл .env
#и возвращать экземпляр класса Config с заполненными полями
#token и admon_ids
def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env("BOT_TOKEN"),
                               admin_ids=list(map(int, env.list("ADMIN_IDS")))))