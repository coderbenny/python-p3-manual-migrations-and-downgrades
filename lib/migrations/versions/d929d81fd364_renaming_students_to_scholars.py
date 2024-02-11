"""Renaming students to scholars

Revision ID: d929d81fd364
Revises: 791279dd0760
Create Date: 2024-02-11 09:58:21.213500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd929d81fd364'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students','scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
