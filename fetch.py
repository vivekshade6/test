import mysql.connector
def fetchData():
    mydb = mysql.connector.connect( host="206.189.142.4", user="root", passwd="Tech$321", database="realestate") 

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM propertyDetails WHERE 1")

    myresult = mycursor.fetchall()
    print(myresult)

fetchData()