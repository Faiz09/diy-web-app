"""create user table

Revision ID: 6eab736a115e
Revises: 
Create Date: 2020-02-17 17:38:23.712811

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '6eab736a115e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(200), nullable=False),
        sa.Column('last_name', sa.String(200), nullable=False),
        sa.Column('email', sa.String(200), nullable=False, unique=True),
        sa.Column('created_at', sa.DateTime()),
        sa.Column('updated_at', sa.DateTime()),
    )


def downgrade():
    op.drop_table('users')
