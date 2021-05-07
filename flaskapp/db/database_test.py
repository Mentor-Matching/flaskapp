
from db_dev import dbServer, port, user, password, database

# import pyodbc
# from sqlalchemy import create_engine
# import urllib

# # params = urllib.parse.quote_plus \ # urllib.parse.quote_plus for python 3
# # (r'Driver={ODBC Driver 13 for SQL Server};Server=tcp:yourDBServerName.database.windows.net,1433;Database=dbname;Uid=username@dbserverName;Pwd=xxx;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
# # conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
# # engine_azure = create_engine(conn_str,echo=True)

# print('connection is ok')
# # print(engine_azure.table_names())

import pyodbc
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:mentormatching-dev.database.windows.net,1433;Database=MentorMatching;Uid=mmDev;Pwd='+ password+ ';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
cursor = conn.cursor()

# cursor = conn.cursor()  
# cursor.execute('SELECT c.CustomerID, c.CompanyName,COUNT(soh.SalesOrderID) AS OrderCount FROM SalesLT.Customer AS c LEFT OUTER JOIN SalesLT.SalesOrderHeader AS soh ON c.CustomerID = soh.CustomerID GROUP BY c.CustomerID, c.CompanyName ORDER BY OrderCount DESC;')  
# row = cursor.fetchone()  
# while row:  
#     print str(row[0]) + " " + str(row[1]) + " " + str(row[2])     
#     row = cursor.fetchone()

# import psycopg


# def create_connection(db_name, db_user, db_password, db_host, db_port):
#     connection = None
#     try:
#         connection = psycopg.connect(
#             database=db_name,
#             user=db_user,
#             password=db_password,
#             host=db_host,
#             port=db_port,
#         )
#         print("Connection to PostgreSQL DB successful")
#     except Exception as e:
#         print(e)
#     return connection


# def create_database(connection, query):
#     connection.autocommit = True
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         print("Query executed successfully")
#     except OperationalError as e:
#         print(f"The error '{e}' occurred")

# connection = create_connection(database, user, password, dbServer, port)
    
# create_database_query = "CREATE DATABASE sm_app"
# create_database(connection, create_database_query)

sslmode = "require"

# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(dbServer, user, database, password, sslmode)
conn = psycopg2.connect(conn_string) 
print("Connection established")