"""empty message

Revision ID: 9642fc8d4a12
Revises: a325595f5939
Create Date: 2020-12-20 23:20:32.465175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9642fc8d4a12'
down_revision = 'a325595f5939'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artists', 'seeking',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('venues', 'seeking',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venues', 'seeking',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('artists', 'seeking',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###
