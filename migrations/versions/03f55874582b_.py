"""empty message

Revision ID: 03f55874582b
Revises: 5469e23edbb0
Create Date: 2018-12-22 22:18:33.444443

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '03f55874582b'
down_revision = '5469e23edbb0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', mysql.VARCHAR(length=16), nullable=False))
    # ### end Alembic commands ###