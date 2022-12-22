import psycopg2

try:
    connection = psycopg2.connect(database="postgres", user="postgres", password="007700", host="127.0.0.1",
                                  port="5432")
    cursor = connection.cursor()

    textfile = 'chartIn.txt'
    with open(textfile) as data:
        lines = data.readlines()[1:]  # skip first two lines
        for line in lines:
            ls = line.split()
            aa, bb, cc, dd, ee, ff = str(ls[1]), str(ls[2]), str(ls[3]), str(ls[4]), str(ls[5]), str(
                ls[6])
            postgres_insert_query = """ INSERT INTO airline_seat (a,b,c,d,e,f) VALUES (%s,%s,%s,%s,%s,%s)"""
            record_to_insert = (aa, bb, cc, dd, ee, ff)
            cursor.execute(postgres_insert_query, record_to_insert)
            # print(aa, bb, cc, dd, ee, ff)

    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into airline_seat table", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


def deletion():
    try:
        connection = psycopg2.connect(database="postgres", user="postgres", password="007700", host="127.0.0.1",
                                      port="5432")
        cur = connection.cursor()
        cur.execute("TRUNCATE TABLE airline_seat RESTART IDENTITY;")
        print("All Records deleted from airline_seat table....")
        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Failed to delete from airline_seat table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

# print("Before deletion")
# deletion()
