"""empty message

Revision ID: 523f24811096
Revises: dee4ed7a556b
Create Date: 2024-02-06 11:19:54.541788

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '523f24811096'
down_revision = 'dee4ed7a556b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sample', schema=None) as batch_op:
        batch_op.add_column(sa.Column('dr_id', sa.String(length=36), nullable=True))
        batch_op.add_column(sa.Column('status', sa.Enum('pending', 'delivering', 'devliverd', name='status'), nullable=True))
        batch_op.add_column(sa.Column('traking_code', sa.String(length=1000), nullable=True))
        batch_op.add_column(sa.Column('result', sa.Text(), nullable=True))
        batch_op.create_foreign_key('fk_sample_to_user_docter', 'users', ['dr_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sample', schema=None) as batch_op:
        batch_op.drop_constraint('fk_sample_to_user_docter', type_='foreignkey')
        batch_op.drop_column('result')
        batch_op.drop_column('traking_code')
        batch_op.drop_column('status')
        batch_op.drop_column('dr_id')

    # ### end Alembic commands ###
