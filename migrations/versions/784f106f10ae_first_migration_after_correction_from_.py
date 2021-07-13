"""first migration after correction from previous migrations.

Revision ID: 784f106f10ae
Revises: 
Create Date: 2021-07-12 23:29:47.034460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '784f106f10ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quran_ayah_text',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('surah_name', sa.String(), nullable=False),
    sa.Column('surah_number', sa.Integer(), nullable=False),
    sa.Column('ayah_arabic', sa.JSON(), nullable=False),
    sa.Column('ayah_indo_pak', sa.LargeBinary(), nullable=True),
    sa.Column('ayah_uthmani', sa.LargeBinary(), nullable=True),
    sa.Column('ayah_number', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quran_ayah_text')
    # ### end Alembic commands ###
