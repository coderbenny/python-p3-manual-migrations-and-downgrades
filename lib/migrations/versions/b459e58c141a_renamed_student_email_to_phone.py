"""Renamed Student email to phone

Revision ID: b459e58c141a
Revises: d929d81fd364
Create Date: 2024-02-11 10:12:15.513175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b459e58c141a'
down_revision = 'd929d81fd364'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars', column_name='email', new_column_name='phone')


def downgrade() -> None:
    op.alter_column('scholars', column_name='phone', new_column_name='email')
