"""empty message

Revision ID: 1f0ce29938a0
Revises: 7fd9213fcf72
Create Date: 2024-03-18 00:31:31.419356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f0ce29938a0'
down_revision = '7fd9213fcf72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=128), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.drop_column('password')

    # ### end Alembic commands ###
