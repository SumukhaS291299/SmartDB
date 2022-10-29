import os
import pickle
import sqlite3
from sqlite3 import OperationalError,NotSupportedError

currDir = os.getcwd()

def CreateDataBase(Dbname:str):
    ChangeDir = pickle.load(open("GITLoc.dat","rb"))
    os.chdir(ChangeDir)
    DB = Dbname+'.db'
    conn = sqlite3.connect(DB)
    if DB in os.listdir():
        try:
            conn.execute("Create Table Billing(slno int not null,Name varchar2 not null,custid primary key not null,cost int not null)")
        except OperationalError:
            print("Table Already exists",OperationalError)
    conn.commit()
    conn.close()
    os.chdir(currDir)

def CreateValues(Dbname:str):
    Dbname = Dbname + ".db"
    ChangeDir = pickle.load(open("GITLoc.dat", "rb"))
    os.chdir(ChangeDir)
    conn = sqlite3.connect(Dbname)
    conn.execute("Insert into Billing values(1,\"SumukhaS\",008,500)")
    conn.execute("Insert into Billing values(2,\"PranavRD\",012,1300)")
    conn.execute("Insert into Billing values(3,\"NitinU\",05,300)")
    conn.commit()
    conn.close()
    os.chdir(currDir)

def Query(Dbname:str):
    Dbname = Dbname + ".db"
    ChangeDir = pickle.load(open("GITLoc.dat", "rb"))
    Dbname = ChangeDir +"/"+ Dbname
    print(Dbname)
    conn = sqlite3.connect(Dbname)
    cursor = conn.execute("select * from Billing")
    for line in cursor:
        print(line)
    cursor = conn.execute("Select count(*) from Billing where cost>100")
    for line in cursor:
        print(line)
    cursor = conn.execute("Select * from Billing order by(cost)")
    for line in cursor:
        print(line)
    conn.commit()
    conn.close()
    os.chdir(currDir)


# CreateDataBase("Sumukha")
# CreateValues("Sumukha")
Query("Sumukha")

