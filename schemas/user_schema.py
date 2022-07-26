from typing import Optional
from pydantic import BaseModel as SCBaseModel

class UserSchema(SCBaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    full_name: str
    job_type: str
    phone: str
    email: str
    image: str
    country: str
    city: str
    onboarding_completion: int

    class Config:
        orm_mode = True