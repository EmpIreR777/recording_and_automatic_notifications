import os
from typing import List

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMIN_IDS: List[int]
    FORMAT_LOG: str = '{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}'
    LOG_ROTATION: str = '10 MB'
    DATABASE_URL: str
    STORE_URL: str
    BASE_SITE: str
    TG_API_SITE: str
    FRONT_SITE: str

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env')
        )

    def get_database_url(self) -> str:
        """Возвращает путь к базе данных"""
        return self.DATABASE_URL

    def get_webhook_url(self) -> str:
        """Возвращаем URL вебхука."""
        return f'{self.BASE_SITE}/webhook'

    def get_tg_api_url(self) -> str:
        """Возвращает URL Telegram API."""
        return f'{self.TG_API_SITE}/bot{self.BOT_TOKEN}'


settings = Settings()
scheduler = AsyncIOScheduler(
    jobstores={'default': SQLAlchemyJobStore(url=settings.STORE_URL)}
        )
