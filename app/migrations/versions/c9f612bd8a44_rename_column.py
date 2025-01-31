"""rename column

Revision ID: c9f612bd8a44
Revises: aaddd1d98502
Create Date: 2024-07-14 19:00:44.873922

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9f612bd8a44'
down_revision: Union[str, None] = 'aaddd1d98502'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hotels', sa.Column('room_quantity', sa.Integer(), nullable=False))
    op.drop_column('hotels', 'room_quamtity')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hotels', sa.Column('room_quamtity', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('hotels', 'room_quantity')
    # ### end Alembic commands ###
