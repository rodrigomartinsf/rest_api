import string
from core.configs import settings
from sqlalchemy import Column, Integer, String

class UserModel(settings.DBBaseModel):
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    first_name: str = Column(String(100))
    last_name: str = Column(String(100))
    full_name: str = Column(String(200))
    job_type: str = Column(String(100))
    phone: str = Column(String(100))
    email: str = Column(String(100))
    image: str = Column(String(300))
    country: str = Column(String(100))
    city: str = Column(String(100))
    onboarding_completion: int = Column(Integer)
