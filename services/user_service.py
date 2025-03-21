from db.db_session import get_session
from repository.user_repository import UserRepository
from schemas.request.user import UserRequestSchema
from schemas.response.user import UserResponseSchema


class UserService:
    """
    Service for users that returns User Data Model Schema.
    """

    def __init__(self):
        session = get_session()
        self.user_repo = UserRepository(db_session=session)

    def get_users(self) -> list[UserResponseSchema]:
        users = self.user_repo.get_users()
        return [
            UserResponseSchema(
                first_name=user.first_name,
                last_name=user.last_name,
                id=user.id).model_dump()
            for user in users
        ]

    def delete_user(self, user_id: int) -> None:
        repo = self.user_repo
        return repo.delete_user(user_id)

    def update_user(self, user_id: int, user_schema: UserRequestSchema) -> UserResponseSchema:
        updated_user = self.user_repo.update_user(user_id, user_schema)
        return UserResponseSchema(first_name=updated_user.first_name, last_name=updated_user.last_name,
                          id=updated_user.id).model_dump()

    def create_user(self, user_schema: UserRequestSchema) -> UserResponseSchema:
        user = self.user_repo.create_user(user_schema)
        return UserResponseSchema(
            first_name=user.first_name,
            last_name=user.last_name,
            id=user.id
        ).model_dump()
