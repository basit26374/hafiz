"""Add sentence sequence

Revision ID: bcb05cc72fd3
Revises: 3e48f0da535f
Create Date: 2021-06-20 23:43:13.972156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcb05cc72fd3'
down_revision = '3e48f0da535f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('quran_sentence_text', sa.Column('sentence_seq', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('quran_sentence_text', 'sentence_seq')
    # ### end Alembic commands ###