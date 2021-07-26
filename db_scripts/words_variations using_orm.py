# import sqlalchemy as db
from sqlalchemy import create_engine, MetaData, Table, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()


engine = create_engine('postgresql+psycopg2://hafiz:hafiz@localhost:5432/hafiz')
Session = sessionmaker(bind = engine)
session = Session()
metadata = MetaData()
metadata.reflect(bind=engine)

# ayah_table = Table('quran_ayah_text', Base.metadata, autoload=True, autoload_with=engine)
class ayah_table(Base):
       __table__ = Table(
          'quran_ayah_text',
          Base.metadata,
          autoload=True,
          autoload_with=engine
       )
# sentence_table = Table('quran_sentence_text', Base.metadata, autoload=True, autoload_with=engine)
class sentence_table(Base):
       __table__ = Table(
          'quran_sentence_text',
          Base.metadata,
          autoload=True,
          autoload_with=engine
       )
# ayah_variations_table = Table('variations', Base.metadata, autoload=True, autoload_with=engine)
class ayah_variations_table(Base):
       __table__ = Table(
          'variations',
          Base.metadata,
          autoload=True,
          autoload_with=engine
       )

class words_table(Base):
       __table__ = Table(
          'quran_word_text',
          Base.metadata,
          autoload=True,
          autoload_with=engine
       )

# class words_table(Base):
#       __tablename__ = 'quran_word_text'

result = session.query(ayah_table).all()
words_record = []
for row in result:
   ayah_id = row.id

   ayah_variations = session.query(ayah_variations_table).filter_by(ayah_text_id = ayah_id).all()
   if ayah_variations:

      for variation in ayah_variations:
             sentence_ids_array = variation.sentence_ids.split('-')

             final_words_array = []
             print('=====================================')
             for indx, sentence_id in enumerate(sentence_ids_array):
                 ayah_sentence = session.query(sentence_table).get(int(sentence_id))
                 # Split ayah sentence into separate words
                 words_array = list(ayah_sentence.sentence_arabic.values())[0].split(' ')

                 if final_words_array:
                     last_word = final_words_array.pop(-1)
                     first_word = words_array.pop(0)
                     combine_word = f'{last_word} {first_word}'

                     final_words_array.insert(len(final_words_array), combine_word)
                     final_words_array.extend(words_array)

                 else:
                     final_words_array.extend(words_array)
             print(final_words_array)

             for word_seq, word in enumerate(final_words_array):
                 rec = words_table(
                    word_seq=word_seq,
                    word_arabic=word,
                    ayah_text_id=ayah_id,
                    ayah_variation_id=variation.id
                 )
                 words_record.append(rec)

session.add_all(words_record)
session.commit()
