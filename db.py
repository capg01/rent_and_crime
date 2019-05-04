import psycopg2

con = psycopg2.connect(
        host = 'localhost',
        database = 'suren',
        user ='postgres'
        )

cur = con.cursor()

cur.execute("SELECT * FROM person")

rows = cur.fetchall()

for pk,name,test,ok,t1,a in rows:
    print(pk)
    print('#'*50)
    print(name)

cur.close()
con.close()
