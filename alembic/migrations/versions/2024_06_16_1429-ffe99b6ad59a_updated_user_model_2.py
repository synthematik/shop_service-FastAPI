"""Updated User model#2

Revision ID: ffe99b6ad59a
Revises: f2d4a280bcc9
Create Date: 2024-06-16 14:29:15.504090

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ffe99b6ad59a'
down_revision: Union[str, None] = 'f2d4a280bcc9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'orders', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'orders', type_='foreignkey')
    op.drop_column('orders', 'user_id')
    # ### end Alembic commands ###