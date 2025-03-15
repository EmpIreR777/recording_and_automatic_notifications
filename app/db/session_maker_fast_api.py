from contextlib import asynccontextmanager
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger

from app.db.database import async_session_maker


class DatabaseSession:
    """
    Класс для управления асинхронными сессиями базы данных.
    Позволяет получать сессию через контекстный менеджер и автоматически
    обрабатывать коммиты, откаты и закрытие сессии.
    """

    @staticmethod
    @asynccontextmanager
    async def get_session(commit: bool = False) -> AsyncGenerator[AsyncSession, None]:
        """
        Асинхронный контекстный менеджер для получения сессии базы данных.
        """
        async with async_session_maker() as session:
            try:
                logger.debug('Сессия базы данных успешно создана')
                yield session
                if commit:
                    await session.commit()
                    logger.debug('Изменения успешно закоммичены')
            except Exception as e:
                logger.error(
                    f'Ошибка в сессии базы данных (commit={commit}): {type(e).__name__}: {e}')
                try:
                    await session.rollback()
                    logger.debug('Откат изменений выполнен')
                except Exception as rollback_error:
                    logger.error(f'Не удалось выполнить откат: {type(rollback_error).__name__}: {rollback_error}')
                raise
            finally:
                await session.close()
                logger.debug('Сессия базы данных закрыта')


db_session = DatabaseSession()
