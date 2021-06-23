"""Create tables

Revision ID: 3e48f0da535f
Revises: 
Create Date: 2021-06-20 21:04:06.040629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e48f0da535f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quran_ayah_text',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('surah_name', sa.String(), nullable=False),
    sa.Column('surah_number', sa.Integer(), nullable=False),
    sa.Column('ayah', sa.LargeBinary(), nullable=False),
    sa.Column('ayah_number', sa.Integer(), nullable=False),
    sa.Column('no_of_sentences', sa.Integer(), nullable=True),
    sa.Column('no_of_words', sa.Integer(), nullable=True),
    sa.Column('no_of_stops', sa.Integer(), nullable=True),
    sa.Column('no_of_variations', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reciter_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('audio_clarity', sa.String(), nullable=True),
    sa.Column('background_noise_level', sa.String(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('with_tajweed', sa.Boolean(), nullable=True),
    sa.Column('number_of_mistakes', sa.Integer(), nullable=True),
    sa.Column('mistakes', sa.JSON(), nullable=True),
    sa.Column('audio_format', sa.String(), nullable=True),
    sa.Column('audio_length_seconds', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('quran_sentence_text',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ayah_number', sa.Integer(), nullable=False),
    sa.Column('surah_number', sa.Integer(), nullable=False),
    sa.Column('sentence_arabic', sa.LargeBinary(), nullable=False),
    sa.Column('ayah_text_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ayah_text_id'], ['quran_ayah_text.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('quran_word_text',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('word_id', sa.Integer(), nullable=False),
    sa.Column('suarh_number', sa.Integer(), nullable=False),
    sa.Column('ayah_number', sa.Integer(), nullable=False),
    sa.Column('word_arabic', sa.LargeBinary(), nullable=False),
    sa.Column('word_english', sa.String(), nullable=True),
    sa.Column('ayah_text_id', sa.Integer(), nullable=False),
    sa.Column('english_translation', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['ayah_text_id'], ['quran_ayah_text.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('variations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_variation', sa.Boolean(), nullable=False),
    sa.Column('ayaah_variations', sa.JSON(), nullable=True),
    sa.Column('ayah_text_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ayah_text_id'], ['quran_ayah_text.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recording_sentence',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recording_sentence', sa.LargeBinary(), nullable=True),
    sa.Column('reciter_info_id', sa.Integer(), nullable=False),
    sa.Column('sentence_text_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['reciter_info_id'], ['reciter_info.id'], ),
    sa.ForeignKeyConstraint(['sentence_text_id'], ['quran_sentence_text.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recording_word',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recording_word', sa.LargeBinary(), nullable=True),
    sa.Column('reciter_info_id', sa.Integer(), nullable=False),
    sa.Column('word_text_id', sa.Integer(), nullable=False),
    sa.Column('recording_sentence_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['reciter_info_id'], ['reciter_info.id'], ),
    sa.ForeignKeyConstraint(['recording_sentence_id'], ['recording_sentence.id'], ),
    sa.ForeignKeyConstraint(['word_text_id'], ['quran_word_text.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recording_word')
    op.drop_table('recording_sentence')
    op.drop_table('variations')
    op.drop_table('quran_word_text')
    op.drop_table('quran_sentence_text')
    op.drop_table('reciter_info')
    op.drop_table('quran_ayah_text')
    # ### end Alembic commands ###