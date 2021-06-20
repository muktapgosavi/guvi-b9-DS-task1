import mysql.connector

hostname = '127.0.0.1'
username = 'MySQL8'
password = 'MysqlRoot@123'
database = 'college'


#import mysql.connector
myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database, auth_plugin='mysql_native_password' )
cur = myConnection.cursor(prepared=True)

def Add_Student():
    try:
        name = input('Enter Name of the Student : ')
        dept = input('Enter Department : ')
        college = input('Enter College name : ')
        m1 =  int(input('Enter Marks of 1st Subject : '))
        m2 =  int(input('Enter Marks of 2nd Subject : '))
        m3 =  int(input('Enter Marks of 3rd Subject : '))
        m4 =  int(input('Enter Marks of 4th Subject : '))
        m5 =  int(input('Enter Marks of 5th Subject : '))
        grade = ''

        total = m1 + m2 + m3 + m4 + m5
        avrage = total//5

        if avrage <= 10 and avrage >= 8:
            grade = 'A'
        elif avrage < 8 and avrage >= 6:
            grade = 'B'
        else :
            grade = 'C'        


        insertStudent = """INSERT into `student`(`Names`, `dept`, `college`, `m1`, `m2`, `m3`, `m4`, `m5`, `total`, `avg`, `grade`) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        val = (name, dept, college, m1, m2, m3, m4, m5, total, avrage, grade)
        cur.execute(insertStudent,val)
        myConnection.commit()

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)

    finally:
        if myConnection.is_connected():
            myConnection.close()
            cur.close()
            print("MySQL connection is closed")





def get_Student():
    try:

        id = int(input('Enter id of the student you want to get details : '))

        cur.execute( "SELECT * FROM student where id= %d"%id)
        result= cur.fetchall()
        myConnection.commit()

        print("\nPrinting each row")
        for row in result:
            print("ID = ", row[0])
            print("Name = ", row[1])
            print("Department = ", row[2])
            print("College  = ", row[3])
            print("Marks of 1st subject  = ", row[4])
            print("Marks of 2nd subject  = ", row[5])
            print("Marks of 3rd subject  = ", row[6])
            print("Marks of 4th subject  = ", row[7])
            print("Marks of 5th subject  = ", row[8])
            print("Total  = ", row[9])
            print("Average  = ", row[10])
            print("Grade  = ", row[11], "\n")

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)

    finally:
        if myConnection.is_connected():
            myConnection.close()
            cur.close()
            print("MySQL connection is closed")




def update_Student():
    try :
        id = int(input('Enter id of the student you want to get details : '))

        name = input('Enter Name of the Student : ')
        dept = input('Enter Department : ')
        college = input('Enter College name : ')
        m1 =  int(input('Enter Marks of 1st Subject : '))
        m2 =  int(input('Enter Marks of 2nd Subject : '))
        m3 =  int(input('Enter Marks of 3rd Subject : '))
        m4 =  int(input('Enter Marks of 4th Subject : '))
        m5 =  int(input('Enter Marks of 5th Subject : '))
        grade = ''

        total = m1 + m2 + m3 + m4 + m5
        avrage = total//5

        if avrage <= 10 and avrage >= 8:
            grade = 'A'
        elif avrage < 8 and avrage >= 6:
            grade = 'B'
        else :
            grade = 'C'        

        cur.execute("Update student Names = '"+name+"', dept = '"+dept+"', college = '"+college+"', m1 ='"+m1+"', m2 = '"+m2+"', m3 = '"+m3+"', m4 = '"+m4+"', m5 = '"+m5+"', total = '"+total+"', avg = '"+avrage+"', grade = '"+grade+"'" )
        myConnection.commit()
    
    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)

    finally:
        if myConnection.is_connected():
            myConnection.close()
            cur.close()
            print("MySQL connection is closed")




def delete_Student():
    try : 
        id = int(input('Enter id of the student you want to get details : '))
        cur.execute("Delete From student where id = '"+id+"'")
        myConnection.commit()

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)

    finally:
        if myConnection.is_connected():
            myConnection.close()
            cur.close()
            print("MySQL connection is closed")




while(True):
    opr=int(input("what you want to do:\n 1. Add Student \n 2. Get Student \n 3. Get all Students \n 4. Update Student \n 5. Delete a Student \n 6. Exit  \n"))

    if opr == 1:
        Add_Student()
        pass


    elif opr == 2:
        get_Student()
        pass


    elif opr == 3 :
        try :
            cur.execute( "SELECT * FROM student ")
            result= cur.fetchall()
            myConnection.commit()
            # print(result)

            print("\nPrinting each row")
            for row in result:
                print("ID = ", row[0])
                print("Name = ", row[1])
                print("Department = ", row[2])
                print("College  = ", row[3])
                print("Marks of 1st subject  = ", row[4])
                print("Marks of 2nd subject  = ", row[5])
                print("Marks of 3rd subject  = ", row[6])
                print("Marks of 4th subject  = ", row[7])
                print("Marks of 5th subject  = ", row[8])
                print("Total  = ", row[9])
                print("Average  = ", row[10])
                print("Grade  = ", row[11], "\n")

        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)

        finally:
            if myConnection.is_connected():
                myConnection.close()
                cur.close()
                print("MySQL connection is closed")

        pass        



    elif opr == 4:
        update_Student()  
        pass



    elif  opr == 5 :
        delete_Student()
        pass

    elif opr == 6:
        print("Exiting Program...")
        break


    else:
        print("invalid choice")   
        break           


