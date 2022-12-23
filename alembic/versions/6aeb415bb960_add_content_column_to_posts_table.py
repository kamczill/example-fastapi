"""add content column to posts table

Revision ID: 6aeb415bb960
Revises: 034e901b0ed0
Create Date: 2022-12-23 09:57:28.032333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6aeb415bb960'
down_revision = '034e901b0ed0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
