import sqlite3
import pymysql

# menentukan tipe koneksi dan melakukan koneksi data
def connect_run(database_name,*args):
    type_data = args[0]
    host = args[1]
    user = args[2]
    password = args[3]
    # database = args[4]
    # import pdb
    # pdb.set_trace()
   # mydatabase = "nama"
    if type_data == 'sqlite' :
        database_name = database_name
        connect = sqlite3.connect(f"py/{database_name}.db")
        connect.close()
        print ('hello semua')
    elif type_data =="mariadb" or type_data == "mysql":
        con = pymysql.connect(host="localhost",user="root",password='',database=database_name)
        cur = con.cursor()
        print (con.cursor())
    return True



