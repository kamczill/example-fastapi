"""add user table

Revision ID: f1557d90d766
Revises: 6aeb415bb960
Create Date: 2022-12-23 10:01:42.359136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1557d90d766'
down_revision = '6aeb415bb960'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),                    
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
