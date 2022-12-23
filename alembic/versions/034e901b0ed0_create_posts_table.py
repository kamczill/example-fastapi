"""create posts table

Revision ID: 034e901b0ed0
Revises: 
Create Date: 2022-12-23 09:42:35.650047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '034e901b0ed0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts", sa.Column('id', sa.Integer(), nullable=False, primary_key=True)
                    , sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
