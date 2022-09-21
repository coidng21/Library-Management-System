def connectDB():
    import mysql.connector

    mysqldb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='password',
        db='business')

    mycursor = mysqldb.cursor()

    return mysqldb, mycursor
