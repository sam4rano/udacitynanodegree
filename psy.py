import psycopg2

hostname = "localhost"
database = "demo_one"
username = "postgres"
pwd="S1a9m9u2$"
port_id = 5432

conn = None
cur = None

conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=5432

    )

cur = conn.cursor()

create_script = ''' CREATE TABLE emp (
        id int PRIMARY KEY,
        name varchar(40) NOT NULL,
        salary int,
        dept_id varchar(30)
    )
    '''
cur.execute(create_script)


insert_script = 'INSERT INTO emp (id,name,salary,dept_id) VALUES(%s,%s,%s,%s)'
insert_value = [(1, 'James',1200,'D4'),(2, 'Cain',1700,'D2'),(3, 'Matt',1500,'D1')]

for record in insert_value:
    cur.execute(insert_script, record)
cur.execute('SELECT * FROM emp')

conn.commit
conn.close()
cur.close()