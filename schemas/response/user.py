from typing import Optional

from schemas.core import UserBaseSchema


class UserResponseSchema(UserBaseSchema):
    id: Optional[int] = None
