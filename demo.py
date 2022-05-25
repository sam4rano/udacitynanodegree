from optparse import Values
import psycopg2

conn = psycopg2.connect('dbname=postgres user=postgres')

cur = conn.cursor()

cur.execute('''
  CREATE TABLE table2 (
      id INTEGER PRIMARY KEY, 
      completed BOOLEAN NOT NULL DEFAULT False  
  );
''')

cur.execute('''INSERT INTO table2 (
    id, completed) VALUES(1, true);''')

conn.commit()

cur.execute('''
  CREATE TABLE table3 (
      id INTEGER PRIMARY KEY, 
      completed BOOLEAN NOT NULL DEFAULT False  
  );
''')

cur.execute('''INSERT INTO table3 (
    id, completed) VALUES(1, true);''')

conn.commit()

conn.close()

cur.close()