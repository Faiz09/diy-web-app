"""create post table

Revision ID: 4a7c5a6e1586
Revises: 6eab736a115e
Create Date: 2020-02-17 17:51:33.206295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a7c5a6e1586'
down_revision = '6eab736a115e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer()),
        sa.Column('title', sa.String(200), nullable=False),
        sa.Column('body', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime()),
        sa.Column('updated_at', sa.DateTime()),
    )

    op.create_foreign_key('fkey_users', 'posts', 'users', ['user_id'], ['id'])


def downgrade():
    op.drop_constraint('fkey_users', 'posts', type_='foreignkey')
    op.drop_table('posts')
