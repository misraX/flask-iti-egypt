"""Adding email, and country to the user table

Revision ID: cb5ac6268b45
Revises: 537e0391f1d7
Create Date: 2025-03-21 23:02:30.774918

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cb5ac6268b45'
down_revision: Union[str, None] = '537e0391f1d7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=50), nullable=True))
    op.add_column('user', sa.Column('country', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'country')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###
