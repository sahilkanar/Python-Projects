import database as db
from database import *
from models import *
import maskpass
from validation import *

print("STUDENT MANAGEMENT SYSTEM".center(80,"🔹"))

choice = 0

while 1 == 1:
    print("1.Admin Login\n2.Student Login\n3.Student Register\n4.Search Courses\n5.Exit")
    choice = int(input("Enter your choice "))
    if choice == 1:
        email = input("Enter your Email ")
        password = maskpass.askpass("Enter your Password ",mask="*")
        valid = db.admin_login(email,password)
        if valid:
            while 1 == 1:
                print("1.Add Student\n2.View Students\n3.Update Student\n4.Delete Student\n5.Add Course\n6.Delete course\n7.View Courses\n8.Exit")
                choice = int(input("Enter your choice "))
                if choice == 1:
                    student_id = input("Enter ID ")
                    student_name = input("Enter Full Name ")
                    phone_no = input("Enter your Phone Number ")
                    if phone_no_validation(phone_no):
                        student_email = input("Enter your email ")
                    else:
                        break
                    if email_validation(student_email) and db.check_user(student_email):
                        student_password = maskpass.askpass("Enter your Password ",mask="*")
                    else:
                        break
                    if password_validation(student_password):
                        course = input("Enter your Course ")
                    else:
                        break
                    if db.search_courses(course):
                        course_code = input("Enter your course code ")
                        db.signup(student_id, student_name, phone_no, student_email, student_password,course,course_code)
                    else:
                        break

                if choice == 2:
                    course_name = input("Enter course name ").lower()
                    db.view_student(course_name)

                if choice == 3:
                    id = int(input("Enter ID "))
                    email = input("Enter Email ")
                    valid = db.check_data(id,email)
                    if valid:
                        while 1 == 1:
                            print("1.Update Name\n2.Update Phone Number\n3.Exit")
                            choice = int(input("Enter your choice "))
                            if choice == 1:
                                old_student_name = input("Enter your old name ")
                                new_student_name = input("Enter your new name ")
                                db.update_name(old_student_name,new_student_name)
                            if choice == 2:
                                old_phone_no = input("Enter old Phone No ")
                                new_phone_no = input("Enter new Phone No ")
                                db.update_phone_no(old_phone_no,new_phone_no)
                            if choice == 3:
                                break

                if choice == 4:
                    id = int(input("Enter ID "))
                    email = input("Enter Email ")
                    db.delete_student(id,email)
                if choice == 5:
                    course_code = input("Enter course code ")
                    course_name = input("Enter course name ")
                    course_duration = input("Enter course duration ")
                    course_timing = input("Enter course timing ")
                    db.add_course(course_code,course_name,course_duration,course_timing)
                if choice == 6:
                    course_name = input("Enter course name you want to delete ").lower()
                    db.delete_course(course_name)
                if choice == 7:
                    course_name = input("Enter course name ").lower()
                    db.view_courses(course_name)
                if choice == 8:
                    break
    if choice == 2:
        student_id = int(input("Enter your ID "))
        email = input("Enter your Email ")
        password = maskpass.askpass("Enter your Password ",mask="*")        
        validdata = db.student_login(email,password)
        if validdata:
            while 1 == 1:
                print("1.Search Courses\n2.Update Data\n3.View Data\n4.Exit")
                choices = int(input("Enter your choice "))
                if choices == 1:
                    course_name = input("Enter course name ").lower()
                    db.search_courses(course_name)
                if choices == 2:
                    done = db.check_data(student_id,email)
                    if done:
                        while 1 == 1:
                            print("1.Update Name\n2.Update Phone Number\n3.Exit")
                            choices = int(input("Enter your choice "))
                            if choices == 1:
                                old_student_name = input("Enter your old name ")
                                new_student_name = input("Enter your new name ")
                                db.update_name(old_student_name,new_student_name)
                            if choices == 2:
                                old_phone_no = input("Enter old Phone No ")
                                new_phone_no = input("Enter new Phone No ")
                                db.update_phone_no(old_phone_no,new_phone_no)
                            if choices == 3:
                                break
                if choices == 3:
                    db.view_data(email)
                if choices == 4:
                    break

    if choice == 3:
        while 1 == 1:
            student_id = input("Enter ID ")
            student_name = input("Enter Full Name ")
            phone_no = input("Enter your Phone Number ")
            if phone_no_validation(phone_no):
                student_email = input("Enter your email ")
            else:
                break
            if email_validation(student_email) and db.check_user(student_email):
                student_password = maskpass.askpass("Enter your Password ",mask="*")
            else:
                break
            if password_validation(student_password):
                course = input("Enter your Course ").lower()
            else:
                break
            if db.search_courses(course):
                course_code = input("Enter your course code ")
                db.signup(student_id, student_name, phone_no, student_email, student_password, course, course_code)
            else:
                break

            break
    if choice == 4:
        course_name = input("Enter course name ").lower()
        db.search_courses(course_name)
    if choice == 5:
        print("Bye!🙋")
        break

