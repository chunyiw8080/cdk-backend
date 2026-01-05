from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from app.db import Base

class CDKey(Base):
    __tablename__ = "cdkeys"

    id = Column(Integer, primary_key=True, index=True)
    cdk = Column(String(64), unique=True, index=True, nullable=False)
    used = Column(Boolean, default=False)
    used_by = Column(Integer, nullable=True)
    used_at = Column(DateTime, nullable=True)
