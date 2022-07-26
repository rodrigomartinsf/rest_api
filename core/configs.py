from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://dtzkwgrmokszmtqholsjfocf@psql-mock-database-cloud:noybogdjtugcxjqvyzfiesuf@psql-mock-database-cloud.postgres.database.azure.com:5432/booking1658833303319rxszjmtjfqfjrfzj"
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()