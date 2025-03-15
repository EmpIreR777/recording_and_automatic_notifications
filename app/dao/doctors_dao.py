from app.schemas.doctors_schemas import BookingSlot
from app.dao.base import BaseDAO
from app.db.models.models import Specialization, Doctor


class DoctorDAO(BaseDAO[Doctor]):
    model = Doctor
