from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger
from app.db.database import async_session_maker


class DatabaseSession:
    """
    Класс для управления асинхронными сессиями базы данных.
    Предоставляет методы для получения сессий с автоматическим коммитом или без него.
    """

    @staticmethod
    async def get_session(commit: bool = False) -> AsyncGenerator[AsyncSession, None]:
        """
        Генератор асинхронной сессии базы данных.

        :param commit: Если True, автоматически коммитит изменения после завершения работы с сессией.
        :return: Асинхронный генератор сессии.
        """
        async with async_session_maker() as session:
            try:
                logger.debug('Сессия базы данных успешно создана')
                yield session
                if commit:
                    await session.commit()
                    logger.debug('Изменения успешно закоммичены')
            except Exception as e:
                logger.error(f'Ошибка в сессии базы данных: {e}')
                await session.rollback()
                logger.debug('Откат изменений выполнен')
                raise
            finally:
                await session.close()
                logger.debug('Сессия базы данных закрыта')

    @staticmethod
    async def get_db() -> AsyncGenerator[AsyncSession, None]:
        """
        Dependency для получения сессии базы данных без автоматического коммита.

        :return: Асинхронный генератор сессии.
        """
        logger.debug('Получение сессии базы данных без автоматического коммита')
        async for session in DatabaseSession.get_session(commit=False):
            yield session

    @staticmethod
    async def get_db_with_commit() -> AsyncGenerator[AsyncSession, None]:
        """
        Dependency для получения сессии базы данных с автоматическим коммитом.

        :return: Асинхронный генератор сессии.
        """
        logger.debug('Получение сессии базы данных с автоматическим коммитом')
        async for session in DatabaseSession.get_session(commit=True):
            yield session


db_session = DatabaseSession()
