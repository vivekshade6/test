# import mysql.connector
# def DataUpdate(name, type, phone,pincode):
#     mydb = mysql.connector.connect( host="206.189.142.4", user="root",  
#     passwd="Tech$321", database="realestate") 
#     mycursor = mydb.cursor() 
#     sql='INSERT INTO users (name, type, phone,pincode) VALUES ("{0}","{1}", "{2}","{3}");'.format(name, type ,phone,pincode) 
#     mycursor.execute(sql) 
#     mydb.commit()
#     mydb.close()
# #     print(mycursor.rowcount,'record inserted.')

import mysql.connector
def DataUpdate(name, phone,pincode): 
    mydb = mysql.connector.connect( host="206.189.142.4", user="root",  
    passwd="Tech$321", database="realestate") 
    mycursor = mydb.cursor() 
    sql='INSERT INTO users (name, phone,pincode) VALUES ("{0}","{1}", "{2}");'.format(name, phone,pincode)
    mycursor.execute(sql) 
    mydb.commit()

# if __name__ =="__main__":
#     DataUpdate("xyz","mid","123456","345678")





# import mysql.connector
# db_connection = mysql.connector.connect(
#   host="206.189.142.4",
#   user="root",
#   passwd="Tech$321"
# )
# print(db_connection)


