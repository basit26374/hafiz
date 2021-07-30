"""Change 'quran_word_text' table.

Revision ID: 01e3ed07968e
Revises: f63127834429
Create Date: 2021-07-25 16:00:22.428656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01e3ed07968e'
down_revision = 'f63127834429'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('quran_word_text', sa.Column('ayah_variation_id', sa.Integer(), nullable=False))
    op.drop_column('quran_word_text', 'word_arabic')
    op.add_column('quran_word_text', sa.Column('word_arabic', sa.String(), nullable=False))
    op.create_foreign_key(None, 'quran_word_text', 'variations', ['ayah_variation_id'], ['id'])
    op.drop_column('quran_word_text', 'ayah_number')
    op.drop_column('quran_word_text', 'surah_number')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('quran_word_text', 'word_arabic')
    op.add_column('quran_word_text', sa.Column('word_arabic', sa.JSON(), nullable=False))
    op.add_column('quran_word_text', sa.Column('surah_number', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('quran_word_text', sa.Column('ayah_number', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'quran_word_text', type_='foreignkey')
    op.drop_column('quran_word_text', 'ayah_variation_id')
    # ### end Alembic commands ###