"""delete vocab

Revision ID: 3552160226c6
Revises: 69386eb05d9c
Create Date: 2020-07-14 22:13:13.560845

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3552160226c6'
down_revision = '69386eb05d9c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dvocab')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dvocab',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('words_es', sa.VARCHAR(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
