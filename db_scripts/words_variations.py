# import sqlalchemy as db
from sqlalchemy import create_engine, MetaData, Table
engine = create_engine('postgresql+psycopg2://hafiz:hafiz@localhost:5432/hafiz')
conn = engine.connect()
metadata = MetaData()
ayah_text = Table('quran_ayah_text', metadata, autoload=True, autoload_with=engine)
sentence_text = Table('quran_sentence_text', metadata, autoload=True, autoload_with=engine)

ayah = ayah_text.select()
result = conn.execute(ayah)
for row in result:
   print (row)