# import sqlalchemy as db
from sqlalchemy import create_engine, MetaData, Table, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from array import array
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

def word_exist(word):
    word_rec = session.query(words_table).filter_by(word_arabic = word).first()
    if word_rec:
        print('exist word_id : ', word_rec.id)
        return True, word_rec.id
    else:
        return False, None

def register_unique_word(word):
    rec = words_table(
        word_arabic=word
    )
    session.add(rec)
    session.commit()
    print('new word_id : ', rec.id)
    return rec.id

def put_word_ids(word_list, ayah_variations_record):
    words_ids = []
    for word in word_list:
        print('word : ', word)
        isexist, word_id = word_exist(word)
        print('isexist, word_id : ', isexist, word_id)
        if isexist:
            words_ids.append(word_id)
        else:
            record_id = register_unique_word(word)
            words_ids.append(record_id)

    print('words_ids : ', words_ids)
    ayah_variations_record.word_ids = array("i", words_ids)
    session.add(ayah_variations_record)
    session.commit()

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
                     combine_word = f'{last_word}-{first_word}'

                     final_words_array.insert(len(final_words_array), combine_word)
                     final_words_array.extend(words_array)

                 else:
                     final_words_array.extend(words_array)
             print(final_words_array)

             put_word_ids(final_words_array, variation)

