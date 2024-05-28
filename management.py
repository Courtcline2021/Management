import mysql.connector
# connects the SQL database to python via pip install 
# not sure if this is going to pull correctly 
try: 
    con = mysql.connector.connect(host="127.0.0.1", user="root", port="3306", database="employee")
except:     

# Function that allows new employees to be added to table 
def add_employ():
    Id = input("Enter employee Id: ")
    if (check_employee(Id) == True):
        print("Employee already exist\nTry again\n")
        menu()
    else: 
        Name = input("Enter employee First Name :  ")   
        Post = input("Enter Employee Post :  ") 
        Salary = input("Enter Employee Salary :  ")
        data = (Id, Name,  Post, Salary)

        sql = 'insert into employee_record values(%s,%s,%s,%s)'
        c = con.cursor()

        c.execute(sql,data)
        con.commit()
        print("Employee Added Successfully")

def promote_employee():
    Id = int(input("Enter Employ's Id :  "))
    if(check_employee(Id) == False):
        print("Employee does not exist\nTry Again\n")
        menu()
    else:
        Amount = int(input("Enter increase in Salary")) 
        sql = 'select salary from employee_record where id=%s'
        data = (Id,)
        c = con.cursor()  
        c.execute(sql,data)
        r = c.fetchone() 
        t = r[0] +Amount
        sql = 'update employee_record set salary=%s where id=%s'
        d = (t,Id)
        c.execute(sql,d)
        con.commit()
        print("Employee Promoted")
        menu()

def remove_employee():
    Id = input("Enter Employee Id :  ")
    if(check_employee(Id) == False):
        print("Employee does not exist\nTry Again\n")
        menu()
    else:
        sql = 'delete from employee_record where id=%s'
        data = (Id,)
        c = con.cursor()
        c.execute(sql,data)
        con.commit()    
        print("Employee Removed")
        menu()

def check_employee(employee_id):
    sql = 'select * from employee_record where id=%s'
    c = con.cursor(buffered=True)
    data = (employee_id,)
    c.execute(sql,data)
    r = c.rowcount
    if r == 1 :
        return True
    else:
        return False

def display_employees():
    sql = 'select * from employee_record'
    c = con.cursor()
    c.execute(sql)
    r = c.fetchall()
    for i in r:
        print('Employee Id : ', i[0])
        print("Employee Name :  ",i[1])
        print("Employee Post : ", i[2])
        print("Employee Salary :  ", i[3])  
        print("------------------\
            -------------------------\
            ----------------------------\
            ------------------------ ") 
    menu()

def menu():
    print("Welcome to Employee Management Record")
    print("Press  ")
    print("1 to Add Employee")
    print("2 to Remove Employee ")
    print("3 to Promote Employee")
    print("4 to Display Employees")
    print("5 to Exit")
    
    ch = int(input("Enter your Choice: "))
    if ch == 1:
        add_employ()
    elif ch == 2:
        remove_employee()
    elif ch == 3:
        promote_employee()
    elif ch == 4:
        display_employees()
    elif ch == 5:
        exit(0)
    else:
        print("Invalid Choice")
        menu()   

menu()