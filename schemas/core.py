from typing import Optional

from pydantic import BaseModel, constr


class UserBaseSchema(BaseModel):
    first_name: constr(
        min_length=1,
        max_length=100,
        pattern='^[a-zA-Z]+$',
    )
    last_name: constr(
        min_length=1,
        max_length=100,
        pattern='^[a-zA-Z]+$',
    )
    email: Optional[str]  = None
    country: Optional[str] = None
