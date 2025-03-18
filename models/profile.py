from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from models import Base


class UserProfile(Base):
    __tablename__ = 'user_profile'
    id: Mapped[int] = mapped_column(primary_key=True)
    profile_picture: Mapped[str] = mapped_column(String(50), nullable=False)
