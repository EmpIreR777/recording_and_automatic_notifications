from datetime import date, datetime, timedelta
from loguru import logger
import pytz
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.specializations_dao import SpecializationDAO
from app.schemas.specializations_schemas import SpecIDModel
from app.db.session_maker_fast_api import db_session

MOSCOW_TZ = pytz.timezone('Europe/Moscow')


router = APIRouter()
