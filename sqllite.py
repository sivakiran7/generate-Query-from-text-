import sqlite3

##connect to sqllite
connection=sqlite3.connect("student.db")

# create a object to insert record,create table

cursor=connection.cursor()

##creat the table
table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25));

"""
cursor.execute(table_info)

##insert some records

cursor.execute(''' Insert Into STUDENT values('Harsha','data science','A') ''')
cursor.execute(''' Insert Into STUDENT values('hemanth','android developer','B') ''')
cursor.execute(''' Insert Into STUDENT values('madhan','devops','C') ''')
cursor.execute(''' Insert Into STUDENT values('venkat','Chemical science','A') ''')
cursor.execute(''' Insert Into STUDENT values('vishnu','fullstack','B') ''')
cursor.execute(''' Insert Into STUDENT values('siva','cyber security','B') ''')



##display records
print("the inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)  

##commit the changes
connection.commit()
connection.close()
