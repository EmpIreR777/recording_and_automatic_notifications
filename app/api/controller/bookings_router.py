from datetime import date
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.bookings_dao import BookingDAO
from app.db.session_maker_fast_api import db_session


router = APIRouter()


@router.get('/booking/available-slots/{doctor_id}')
async def get_available_slots(
    doctor_id: int, start_date: date,
    session: AsyncSession = Depends(db_session.get_session)):
    return await BookingDAO.get_available_slots(session=session, doctor_id=doctor_id, start_date=start_date)
