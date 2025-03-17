from fastapi import APIRouter, Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.async_client import http_client_manager
from app.db.session_maker_fast_api import db_session
from app.tg_bot.handlers import (
    cmd_start, handler_my_appointments, handler_about_us, handler_back_home,
    handler_my_appointments_all,
    )
