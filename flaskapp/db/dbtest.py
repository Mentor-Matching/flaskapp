import pymysql

# cnx = mysql.connector.connect(user="mmDev@mm-mariadb-dev", password="MentorMatching!", host="mm-mariadb-dev.mariadb.database.azure.com", port=3306, database="MentorMatching")

connection = pymysql.connect(host='mm-mariadb-dev.mariadb.database.azure.com',
                             user='mmDev@mm-mariadb-dev',
                             password='MentorMatching!',
                             database='MentorMatching',
                             cursorclass=pymysql.cursors.DictCursor)

# with connection:
#     with connection.cursor() as cursor:
#         # Create a new record
#         cursor.execute("SELECT VERSION()")
        # sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        # cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    # connection.commit()

    # with connection.cursor() as cursor:
        # Read a single record
        # sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        # cursor.execute(sql, ('webmaster@python.org',))
        # result = cursor.fetc
# connection.close()