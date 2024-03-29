"""empty message

Revision ID: 20b110a1b4ad
Revises: eb8e866525ab
Create Date: 2024-02-03 20:00:05.050376

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20b110a1b4ad'
down_revision = 'eb8e866525ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_type', sa.Enum('Not_given', 'A_positive', 'A_negative', 'B_positive', 'B_negative', 'O_positive', 'O_negative', 'AB_positive', 'AB_negative', name='usertype'), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('user_type')

    # ### end Alembic commands ###
