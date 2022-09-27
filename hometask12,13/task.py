import pymysql


conn = pymysql.connect(
    host='localhost',
    user='root',
    password="root",
    db='training',
)

cur = conn.cursor()

cur.execute("SELECT COUNT(students.subject) FROM students INNER JOIN audience ON audience.subject = students.subject WHERE students.subject='ОСиСП'")
print(cur.fetchone()[0])
conn.commit()

conn.close()
