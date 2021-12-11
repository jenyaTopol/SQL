import sqlite3

# if exists that connects to it ...
# if not exist - it creates it for us
conn = sqlite3.connect(r'C:\Users\jenya\Desktop\sqlite\product.db') # FIX this!!!!!!!!!!!! *your path
print ("Opened database successfully")

def print_table_company(cond = ''):
    cursor = conn.execute("SELECT * from COMPANY" + cond)
    #print(cursor)
    for row in cursor:
        print(f'ID: {row[0]}, NAME: {row[1]}, AGE: {row[2]}, ADDRESS: {row[3]}, SALARY: {row[4]}')

def insert_into_table_company(emp):
    conn.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) "\
                    f"VALUES ('{emp.name}',{emp.age},'{emp.address}',{emp.salary});");
    # must COMMIT !!!! [git]
    conn.commit()
    print(f"employee {emp.name} was inserted into COMPANY table")

class Employee:
    def __init__(self, id, name, age, address, salary):
        self.id = id
        self.name = name
        self.age = age
        self.address = address
        self.salary = salary

print('== print table company no condition ==')
print_table_company()
print('== print table company condition: WHERE AGE > 24 ==')
print_table_company(' WHERE AGE > 24')

tim = Employee(0, 'Tim Robbins', 45, 'Holland', 55400)
insert_into_table_company(tim)

print('== print table company no condition ==')
print_table_company()

print('=============================== tagril 2 =====================')
'''
1. run queries from previous targil (1-4) using this method:
        print_table_company
        (never mind select specific columns)
2. insert two new rows into databse (age will be above 40)
    create new Employee for each one (like Tim Robbins we did here) 
    using this method: insert_into_table_company
3. create new table of COMPANY_ELDER
        conn.execute("CREATE TABLE ...."); # no need commit? try?
        conn.execute("INSERT ... SELECT ...")
        *etgar: can you make it a function?
4. *etgar: can you create a list of Employee as a result value from print_table_company  
'''

print('===================== solution =============')
# 1. run queries from previous targil (1-4) using this method:
print_table_company() #1
print_table_company(' WHERE SALARY > 40000') #2
print_table_company(' WHERE SALARY > (SELECT AVG(SALARY) FROM COMPANY)') #3
print_table_company(' WHERE SALARY = (SELECT MAX(SALARY) FROM COMPANY)') #4

'''
longer:
cursor = conn.execute("SELECT * from COMPANY WHERE SALARY > 40000")
# print(cursor)
for row in cursor:
    print(f'ID: {row[0]}, NAME: {row[1]}, AGE: {row[2]}, ADDRESS: {row[3]}, SALARY: {row[4]}')
    
cursor = conn.execute("SELECT * from COMPANY WHERE SALARY > (SELECT AVG(SALARY) FROM COMPANY)")
# print(cursor)
for row in cursor:
    print(f'ID: {row[0]}, NAME: {row[1]}, AGE: {row[2]}, ADDRESS: {row[3]}, SALARY: {row[4]}')
.....    
'''

jobs = Employee(0, 'steve jobs', 55, 'USA New york', 159832)
insert_into_table_company(jobs)
mark = Employee(0, 'mark cohen', 49, 'fiji islands', 43222)
insert_into_table_company(mark)
'''
conn.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) "\
            f"VALUES ('steve jobs',55,'USA New york',159832);");
conn.commit()
...
'''

# create table does not require commit
conn.execute('CREATE TABLE "COMPANY_ELDERS" ("ID"	INTEGER NOT NULL,"NAME"	TEXT NOT NULL,"AGE"	INT NOT NULL,"ADDRESS"	CHAR(50),"SALARY"	REAL,PRIMARY KEY("ID" AUTOINCREMENT));')

conn.execute("INSERT INTO COMPANY_ELDERS(NAME, AGE, ADDRESS, SALARY)"\
" SELECT NAME, AGE, ADDRESS, SALARY FROM COMPANY "\
"WHERE AGE >  40;")
conn.commit()
