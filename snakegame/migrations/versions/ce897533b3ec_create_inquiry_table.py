import sqlalchemy as sa

from alembic import op

from lib.util_datetime import tzware_datetime
from lib.util_sqlalchemy import AwareDateTime


"""
create inquiry table

Revision ID: ce897533b3ec
Revises: 
Create Date: 2021-12-03 03:42:59.410281
"""

# Revision identifiers, used by Alembic.
revision = 'ce897533b3ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
