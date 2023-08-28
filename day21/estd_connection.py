# if we want to connect database from a program(pyhton,javascript) then we need a database connector
# database connector connects your proggram with database
# psycopg2 is the example of such connector



def estd_connection():
    import psycopg2
    conn=psycopg2.connect(
        database="student_test_db",
        user="postgres",
        password="@hybesty123",
        host="127.0.0.1",
        port=5432
    )
    conn.autocommit=True
    print("connection is established successfully")
    cursor=conn.cursor()
    return cursor
if __name__=="__main__":
    estd_connection()