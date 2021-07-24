# import sqlalchemy as db
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()


engine = create_engine('postgresql+psycopg2://hafiz:hafiz@localhost:5432/hafiz')
Session = sessionmaker(bind = engine)
session = Session()
metadata = MetaData()

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

result = session.query(ayah_table).all()

for row in result:
   ayah_id = row.id

   ayah_variations = session.query(ayah_variations_table).filter_by(ayah_text_id = ayah_id).all()
   if ayah_variations:

      for variation in ayah_variations:
             sentence_ids_array = variation.sentence_ids.split('-')
            
             last_word, first_word = None, None
             final_words_array = []
             if len(sentence_ids_array) == 1:
               print('=======================')
               ayah_sentence = session.query(sentence_table).get(int(sentence_ids_array[0]))
               words_array = list(ayah_sentence.sentence_arabic.values())[0].split(' ')
               print(words_array)

             elif len(sentence_ids_array) == 2:
                print('-----------------')
                for idx, sent_id in enumerate(sentence_ids_array):
                    ayah_sentence = session.query(sentence_table).get(int(sent_id))
                    words_array = list(ayah_sentence.sentence_arabic.values())[0].split(' ')
                    print(words_array)
                    if last_word:
                       first_word = words_array.pop(0)
                       combine_word = f'{last_word} {first_word}'
                       words_array.insert(0, combine_word)
                       last_word = None
                       
                    if idx == 0:
                        last_word = words_array.pop(-1)       # pop the last word of ayah_sentence (first element of list)
                        final_words_array.extend(words_array)
                    else:
                        final_words_array.extend(word for word in words_array)

                print(final_words_array)
                

# row = result[0]
# print(row.id)
# ayah_id = row.id
# ayah_sentences = session.query(sentence_table).filter(sentence_table.sentence_seq==1).all()
# print(ayah_sentences)
