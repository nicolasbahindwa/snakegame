import sqlalchemy as sa

from alembic import op

from lib.util_datetime import tzware_datetime
from lib.util_sqlalchemy import AwareDateTime
from sqlalchemy.dialects import postgresql

"""
add secret_pharase to users

Revision ID: b0fbd2eb478c
Revises: 0f38a0f403db
Create Date: 2021-12-03 06:08:55.943862
"""

# Revision identifiers, used by Alembic.
revision = 'b0fbd2eb478c'
down_revision = '0f38a0f403db'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('secret_phrase', sa.String(length=128), nullable=True))
    op.create_index(op.f('ix_users_secret_phrase'), 'users', ['secret_phrase'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_secret_phrase'), table_name='users')
    op.drop_column('users', 'secret_phrase')
    ### end Alembic commands ###
