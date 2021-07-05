"""add ayah_arabic field.

Revision ID: 714bbca06b59
Revises: 6d0e03004042
Create Date: 2021-06-29 22:54:27.195822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '714bbca06b59'
down_revision = '6d0e03004042'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('quran_ayah_text', sa.Column('ayah_arabic', sa.JSON(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('quran_ayah_text', 'ayah_arabic')
    # ### end Alembic commands ###