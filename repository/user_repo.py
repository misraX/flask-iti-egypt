from typing import TypeVar, Any

from sqlalchemy.orm import Session

from models.user import User
from schemas.user import UserSchema

_T = TypeVar("_T", bound=Any)


class UserRepository:
    """
    Repository for users, that returns User Model.
    """

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_users(self) -> list[_T]:
        with self.db_session as session:
            users = session.query(User).all()
            if not users:
                return []
            return users

    def delete_user(self, user_id: int) -> None:
        with self.db_session as session:
            user = session.query(User).get(user_id)
            if user:
                session.delete(user)
                session.commit()

    def update_user(self, user_id: int, user_schema: UserSchema) -> User:
        last_name = user_schema.last_name
        first_name = user_schema.first_name
        with self.db_session as session:
            user = session.query(User).get(user_id)
            if user:
                user.last_name = last_name
                user.first_name = first_name
            session.commit()
            session.refresh(user)
            return user
