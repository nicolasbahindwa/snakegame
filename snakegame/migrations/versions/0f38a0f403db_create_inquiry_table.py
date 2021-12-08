import sqlalchemy as sa
from sqlalchemy.sql.expression import true

from alembic import op

from lib.util_datetime import tzware_datetime
from lib.util_sqlalchemy import AwareDateTime


"""
create inquiry table

Revision ID: 0f38a0f403db
Revises: ce897533b3ec
Create Date: 2021-12-03 03:44:18.110783
"""

# Revision identifiers, used by Alembic.
revision = '0f38a0f403db'
down_revision = 'ce897533b3ec'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('inquiry',
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('name', sa.String),
                    sa.Column('message', sa.Text),
                    sa.Column('create_on', AwareDateTime(),
                              default=tzware_datetime),
                    sa.Column('upated_on', AwareDateTime(),
                              default=tzware_datetime,
                              onupdate=tzware_datetime),
                    sa.Column('status', sa.String(128), index=True))


def downgrade():
    op.drop_table('inquiry')
