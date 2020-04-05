"""empty message

Revision ID: 1363be0eef36
Revises: 446a99a51061
Create Date: 2020-04-05 19:47:53.893410

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1363be0eef36'
down_revision = '446a99a51061'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Artist', 'seeking_venue',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('Venue', 'seeking_talent',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Venue', 'seeking_talent',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('Artist', 'seeking_venue',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###
