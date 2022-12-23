"""add last few columns to posts table

Revision ID: 713d8247fe5a
Revises: 5e85a372bb20
Create Date: 2022-12-23 10:18:06.212867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '713d8247fe5a'
down_revision = '5e85a372bb20'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
