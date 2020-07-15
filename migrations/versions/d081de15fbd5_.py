"""empty message

Revision ID: d081de15fbd5
Revises: 5318ff417e8e
Create Date: 2020-07-15 18:58:52.920976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd081de15fbd5'
down_revision = '5318ff417e8e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'association', 'vocab', ['vocab_id'], ['id'])
    op.add_column('vocab', sa.Column('def_es', sa.String(length=1000), nullable=True))
    op.add_column('vocab', sa.Column('form', sa.Integer(), nullable=True))
    op.add_column('vocab', sa.Column('frequency', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vocab', 'frequency')
    op.drop_column('vocab', 'form')
    op.drop_column('vocab', 'def_es')
    op.drop_constraint(None, 'association', type_='foreignkey')
    # ### end Alembic commands ###
