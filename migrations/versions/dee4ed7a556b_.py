"""empty message

Revision ID: dee4ed7a556b
Revises: 47a8fae91bba
Create Date: 2024-02-06 09:57:50.917261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dee4ed7a556b'
down_revision = '47a8fae91bba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('delivery',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('address', sa.Text(), nullable=True),
    sa.Column('slug', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sample_type',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('type', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sample',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('user_id', sa.String(length=36), nullable=False),
    sa.Column('laboratory_id', sa.String(length=36), nullable=True),
    sa.Column('sample_type_id', sa.String(length=36), nullable=True),
    sa.ForeignKeyConstraint(['laboratory_id'], ['laboratory.id'], name='fk_sample_to_laboratory'),
    sa.ForeignKeyConstraint(['sample_type_id'], ['sample_type.id'], name='fk_sample_to_sampletype'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_sample_to_user'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('laboratory_address', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=36),
               existing_nullable=False)

    with op.batch_alter_table('laboratory_branch', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=36),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('laboratory_branch', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.String(length=36),
               type_=sa.INTEGER(),
               existing_nullable=False)

    with op.batch_alter_table('laboratory_address', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.String(length=36),
               type_=sa.INTEGER(),
               existing_nullable=False)

    op.drop_table('sample')
    op.drop_table('sample_type')
    op.drop_table('delivery')
    # ### end Alembic commands ###