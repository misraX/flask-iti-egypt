from typing import Optional

from pydantic import BaseModel


class UserSchema(BaseModel):
    first_name: str
    last_name: str
    id: Optional[int] = None
