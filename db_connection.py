import psycopg2 as ps
# define credentials 
credentials = {'POSTGRES_ADDRESS' : 'hafizdb.cewge3xw8gjx.us-east-2.rds.amazonaws.com', # change to your endpoint
               'POSTGRES_PORT' : '5432', # change to your port
               'POSTGRES_USERNAME' : 'hafiz', # change to your username
               'POSTGRES_PASSWORD' : 'Yu4t3qJnPuy9HJKQeO6u', # change to your password
               'POSTGRES_DBNAME' : 'hafizdb'} # change to your db name
# create connection and cursor    
conn = ps.connect(host=credentials['POSTGRES_ADDRESS'],
                  database=credentials['POSTGRES_DBNAME'],
                  user=credentials['POSTGRES_USERNAME'],
                  password=credentials['POSTGRES_PASSWORD'],
                  port=credentials['POSTGRES_PORT'])
cur = conn.cursor()
