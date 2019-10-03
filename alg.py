import pymysql.cursors

# Connect to the database
connection = pymysql.connect(
    host='localhost',
    user='lucy',
    password='DV5on7ey',
    db='test_database',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

def main():
    try:
        with connection.cursor() as cursor:
            sql = "CREATE TABLE `users`"
            cursor.execute(sql)
        connection.commit()
    finally:
        connection.close()

def example():
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
            cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            cursor.execute(sql, ('webmaster@python.org',))
            result = cursor.fetchone()
            print(result)
    finally:
        connection.close()

main()