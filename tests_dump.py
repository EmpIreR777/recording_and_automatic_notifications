import asyncio
from datetime import datetime, time, date
from faker import Faker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.db.database import Base
from app.db.models.models import User, Doctor, Specialization, Booking

DATABASE_URL = "sqlite+aiosqlite:///data/db.sqlite3"

# Устанавливаем русскую локаль для Faker
fake = Faker('ru_RU')


async def create_fake_data():
    engine = create_async_engine(DATABASE_URL, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async with async_session() as session:
        # Создаем 10 специализаций
        specializations = []
        for _ in range(10):
            specialization = Specialization(
                description=fake.text(max_nb_chars=200),  # Описание специализации
                icon=fake.word(),  # Иконка
                label=fake.word(),  # Название
                specialization=fake.job(),  # Специализация
            )
            specializations.append(specialization)
            session.add(specialization)
        await session.commit()

        # Создаем 10 врачей
        doctors = []
        for _ in range(10):
            doctor = Doctor(
                first_name=fake.first_name_male(),  # Имя (мужское)
                last_name=fake.last_name_male(),  # Фамилия (мужская)
                patronymic=fake.middle_name_male(),  # Отчество (мужское)
                special=fake.job(),  # Специальность
                specialization_id=fake.random_element(
                    elements=[s.id for s in specializations]
                ),  # Связь со специализацией
                work_experience=fake.random_int(min=1, max=30),  # Опыт работы (в годах)
                experience=fake.text(max_nb_chars=200),  # Описание опыта
                description=fake.text(max_nb_chars=200),  # Описание врача
                photo=fake.image_url(),  # Ссылка на фото
            )
            doctors.append(doctor)
            session.add(doctor)
        await session.commit()

        # Создаем 10 пользователей
        users = []
        for _ in range(10):
            user = User(
                telegram_id=fake.random_int(min=100000000, max=999999999),  # ID Telegram
                username=fake.user_name(),  # Имя пользователя
                first_name=fake.first_name(),  # Имя
                last_name=fake.last_name(),  # Фамилия
            )
            users.append(user)
            session.add(user)
        await session.commit()

        # Создаем 10 бронирований
        for _ in range(10):
            booking = Booking(
                doctor_id=fake.random_element(elements=[d.id for d in doctors]),  # Связь с врачом
                user_id=fake.random_element(elements=[u.id for u in users]),  # Связь с пользователем
                day_booking=fake.date_between(start_date='-30d', end_date='+30d'),  # Дата бронирования
                time_booking=fake.time_object(),  # Время бронирования
                booking_status=fake.random_element(
                    elements=['ожидание', 'подтверждено', 'отменено']
                ),  # Статус бронирования
                created_at=datetime.now(),  # Дата создания записи
            )
            session.add(booking)
        await session.commit()


if __name__ == "__main__":
    asyncio.run(create_fake_data())
