"""empty message

Revision ID: 72fa6a192b69
Revises: bc67d3694c3f
Create Date: 2024-02-04 09:21:27.853665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72fa6a192b69'
down_revision = 'bc67d3694c3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('laboratory',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('employee', sa.Integer(), nullable=True),
    sa.Column('year_founded', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('laboratory_branch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('laboratory_id', sa.String(length=36), nullable=False),
    sa.Column('branch_name', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['laboratory_id'], ['laboratory.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('weight',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('weight',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=True)

    op.drop_table('laboratory_branch')
    op.drop_table('laboratory')
    op.drop_table('address')
    # ### end Alembic commands ###
