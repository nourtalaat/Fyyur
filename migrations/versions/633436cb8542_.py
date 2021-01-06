"""empty message

Revision ID: 633436cb8542
Revises: eabd148d5313
Create Date: 2020-12-22 17:09:58.297078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '633436cb8542'
down_revision = 'eabd148d5313'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artists', 'city',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('artists', 'genres',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('artists', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('artists', 'phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('artists', 'state',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artists', 'state',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('artists', 'phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('artists', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('artists', 'genres',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('artists', 'city',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    # ### end Alembic commands ###
