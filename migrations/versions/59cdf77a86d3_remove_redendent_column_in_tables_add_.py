"""Remove redendent column in tables. Add ayaah indo_pak and uthmani into table.

Revision ID: 59cdf77a86d3
Revises: 3a68acad78c1
Create Date: 2021-06-27 10:28:53.521145

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '59cdf77a86d3'
down_revision = '3a68acad78c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('quran_ayah_text', sa.Column('ayah_arabic', sa.LargeBinary(), nullable=False))
    op.add_column('quran_ayah_text', sa.Column('ayah_indo_pak', sa.LargeBinary(), nullable=True))
    op.add_column('quran_ayah_text', sa.Column('ayah_uthmani', sa.LargeBinary(), nullable=True))
    op.drop_column('quran_ayah_text', 'no_of_words')
    op.drop_column('quran_ayah_text', 'ayah')
    op.drop_column('quran_ayah_text', 'no_of_stops')
    op.drop_column('quran_ayah_text', 'no_of_sentences')
    op.drop_column('quran_ayah_text', 'no_of_variations')
    op.add_column('quran_sentence_text', sa.Column('sentence_indo_pak', sa.LargeBinary(), nullable=True))
    op.add_column('quran_sentence_text', sa.Column('sentence_uthmani', sa.LargeBinary(), nullable=True))
    op.add_column('quran_sentence_text', sa.Column('english_transliteration', sa.String(), nullable=True))
    op.drop_column('quran_word_text', 'word_english')
    op.drop_column('quran_word_text', 'english_translation')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('quran_word_text', sa.Column('english_translation', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('quran_word_text', sa.Column('word_english', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('quran_sentence_text', 'english_transliteration')
    op.drop_column('quran_sentence_text', 'sentence_uthmani')
    op.drop_column('quran_sentence_text', 'sentence_indo_pak')
    op.add_column('quran_ayah_text', sa.Column('no_of_variations', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('quran_ayah_text', sa.Column('no_of_sentences', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('quran_ayah_text', sa.Column('no_of_stops', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('quran_ayah_text', sa.Column('ayah', postgresql.BYTEA(), autoincrement=False, nullable=False))
    op.add_column('quran_ayah_text', sa.Column('no_of_words', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('quran_ayah_text', 'ayah_uthmani')
    op.drop_column('quran_ayah_text', 'ayah_indo_pak')
    op.drop_column('quran_ayah_text', 'ayah_arabic')
    # ### end Alembic commands ###
