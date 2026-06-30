from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.database.session import Base


class Machine(Base):
    __tablename__ = "machines"

    id = Column(Integer, primary_key=True, index=True)

    machine_code = Column(String(50), unique=True, nullable=False)
    machine_name = Column(String(100), nullable=False)

    machine_type = Column(String(100), nullable=False)

    location = Column(String(100), nullable=False)

    status = Column(String(30), default="Running")

    health_score = Column(Integer, default=100)

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())