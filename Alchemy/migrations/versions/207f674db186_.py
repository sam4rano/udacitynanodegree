"""empty message

Revision ID: 207f674db186
Revises: 23cdd78b245d
Create Date: 2022-06-07 18:56:40.246029

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '207f674db186'
down_revision = '23cdd78b245d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('persons')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('persons',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='persons_pkey')
    )
    op.drop_table('todo')
    # ### end Alembic commands ###