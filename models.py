
class Student:
    def __init__(self,student_id,student_name,phone_no,student_email,student_password,course,course_code):
        self.student_id = student_id
        self.student_name = student_name
        self.phone_no = phone_no
        self.student_email = student_email
        self.student_password = student_password
        self.course = course
        self.course_code = course_code

    def __str__(self):
        return f"{self.student_id},{self.student_name},{self.phone_no},{self.student_email},{self.student_password},{self.course},{self.course_code}"


class Course:
    def __init__(self,course_code,course_name,course_duration,course_timing):
        self.course_code = course_code
        self.course_name = course_name
        self.course_duration = course_duration
        self.course_timing = course_timing

    def __str__(self):
        return f"{self.course_code},{self.course_name},{self.course_duration},{self.course_timing}"


