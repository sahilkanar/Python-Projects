import mysql.connector as con
import pywhatkit as pt
from colorama import Fore,Back,Style
from validation import *
from prettytable import PrettyTable

try:
    conn = con.connect(host="localhost",user="root",password="sahil@51",database="basicdb")
    cursor = conn.cursor()
except Exception as e:
    print(e)


def signup(student_id,student_name,phone_no,student_email,student_password,course,course_code):
    try:
        cursor.execute(f"insert into student values('{student_id}','{student_name}','{phone_no}','{student_email}','{student_password}','{course}','{course_code}');")
        conn.commit()
        print(Fore.GREEN+"Registered Successfully")
        print(Style.RESET_ALL)
        pt.sendwhatmsg_instantly("+91"+phone_no,f"Congratulations👍\nThank you {student_name} 😍😍 for Choosing {course} course!!!\nYour {course} Batch will start soon")
        print(Fore.CYAN+"Check your Phone")
        print(Style.RESET_ALL)
    except Exception as e:
        print(e)


def admin_login(username,password):
    try:
        cursor.execute("select * from admin;")
        for i in cursor:
            if username == i[0] and password == i[1]:
                print(Fore.GREEN+"Logged in Successfully")
                print(Style.RESET_ALL)
                return True
        else:
            print(Fore.RED+"Invalid Credentials")
            print(Style.RESET_ALL)
            return False
    except Exception as e:
        print(e)


def student_login(student_email,student_password):
    try:
        h = 0
        cursor.execute("select student_email,student_password from student;")
        for i in cursor:
            if student_email == i[0] and student_password == i[1]:
                h = 1

        if h == 1:
            print(Fore.GREEN+"Logged in Successfully")
            print(Style.RESET_ALL)
            return True
        else:
            print(Fore.RED+"Invalid Credentials")
            print(Style.RESET_ALL)
            return False
    except Exception as e:
        print(e)


def check_data(student_id,student_email):
    try:
        h = 0
        cursor.execute("select student_id,student_email from student;")
        for i in cursor:
            if student_id == i[0] and student_email == i[1]:
                h = 1

        if h == 1:
            print(Fore.GREEN+"Record Exists")
            print(Style.RESET_ALL)
            return True
        else:
            print(Fore.RED+"No such record")
            print(Style.RESET_ALL)
            return False
    except Exception as e:
        print(e)


def view_student(course_name):
    try:
        h = 0
        if search_courses(course_name):
            cursor.execute(f"select student_id,student_name,student_email,phone_no,course_name,course_duration,course_timing from student inner join course on student.course_code=course.course_code where course_name='{course_name}';")
            my_table = PrettyTable([Fore.MAGENTA+"student_id","student_name","student_email","phone_no","course_name","course_duration","course_timing"])
            
            for i in cursor:
                my_table.add_row(i)
                print(my_table)
                print(Style.RESET_ALL)
                h = 1
                
                    
            if h == 0:
                print(Fore.RED+"No such Record")
                print(Style.RESET_ALL)
    except Exception as e:
        print(e)



def update_name(old_student_name,new_student_name):
    try:
        h = 0
        cursor.execute(f"select student_name from student where student_name='{old_student_name}';")
        for i in cursor:
            if i[0] == old_student_name:
                h = 1

        if h == 1:
            cursor.execute(f"update student set student_name='{new_student_name}' where student_name='{old_student_name}';")
            conn.commit()
            print(Fore.GREEN+"Name Updated Successfully")
            print(Style.RESET_ALL)
        else:
            print(Fore.RED+"Enter Name Correctly")
            print(Style.RESET_ALL)
    except Exception as e:
        print(e)

def update_phone_no(old_phone_no,new_phone_no):
    try:
        h = 0
        cursor.execute(f"select phone_no from student where phone_no='{old_phone_no}';")
        for i in cursor:
            if i[0] == old_phone_no:
                h = 1

        if h == 1:
            cursor.execute(f"update student set phone_no='{new_phone_no}' where phone_no='{old_phone_no}';")
            conn.commit()
            print(Fore.GREEN+"Phone No Updated Successfully")
            print(Style.RESET_ALL)
        else:
            print(Fore.RED+"Enter Phone Number Correctly")
            print(Style.RESET_ALL)
    except Exception as e:
        print(e)


def delete_student(student_id,student_email):
    try:
        if check_data(student_id,student_email):
            cursor.execute(f"delete from student where student_id='{student_id}' and student_email='{student_email}';")
            conn.commit()
            print(Fore.GREEN+"Deleted Successfully")
            print(Style.RESET_ALL)
        else:
            print(Fore.RED+"No Such Record")
            print(Style.RESET_ALL)
    except Exception as e:
        print(e)


def view_courses(course_name):
    try:
        h=0
        cursor.execute(f"select * from course where course_name='{course_name}';")
        my_table = PrettyTable([Fore.MAGENTA+"course_code","course_name","course_duration","course_timing"])
        for i in cursor:
            my_table.add_row(i)
            
        print(my_table)
        print(Style.RESET_ALL)
    except Exception as e:
        print(e)


def add_course(course_code,course_name,course_duration,course_timing):
    try:
        cursor.execute(f"insert into course values('{course_code}','{course_name}','{course_duration}','{course_timing}');")
        conn.commit()
    except Exception as e:
        print(e)


def delete_course(course_name):
    try:
        if search_courses(course_name):
            cursor.execute(f"delete from course where course_name='{course_name}';")
            conn.commit()
            print(Fore.GREEN+"Deleted Successfully")
            print(Style.RESET_ALL)
    except Exception as e:
        print(e)
    


def search_courses(course_name):
    try:
        h = 0
        cursor.execute(f"select course_name from course where course_name='{course_name}';")
        for i in cursor:
            if i[0].lower() == course_name:
                h = 1

        if h == 1:
            print(Fore.GREEN+course_name,"Course Available")
            print(Style.RESET_ALL)
            return True
        else:
            print(Fore.RED+course_name,"Course Not Available")
            print(Style.RESET_ALL)
            return False
    except Exception as e:
        print(e)


def check_user(student_email):
    try:
        h=0
        cursor.execute("select student_email from student;")
        for i in cursor:
            for j in i:
                if j == student_email:
                    h=1

        if h == 1:
            print("You've already applied for some other course")
            return False
        
        else:
            print("Valid")
            return True
    except Exception as e:
        print(e)


def view_data(email):
    try:
        h=0
        cursor.execute(f"select student_id,student_name,student_email,phone_no,course_name,course_duration,course_timing from student inner join course on student.course_code=course.course_code where student_email='{email}';")
        my_table = PrettyTable([Fore.MAGENTA+"student_id","student_name","student_email","phone_no","course_name","course_duration","course_timing"])
        for i in cursor:
                my_table.add_row(i)
                print(my_table)
                print(Style.RESET_ALL)
                h = 1
                
                    
        if h == 0:
            print(Fore.RED+"No such Record")
            print(Style.RESET_ALL)
    except Exception as e:
        print(e)