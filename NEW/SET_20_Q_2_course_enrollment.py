class CourseFullError(Exception):
    pass


class Course:
    def __init__(self):
        self.students = []

    def enroll_student(self, name):
        pass


class FreeCourse(Course):
    def enroll_student(self, name):
        self.students.append(name)
        print("Enrolled:", name)


class PaidCourse(Course):
    def enroll_student(self, name, payment):
        if len(self.students) >= 2:
            raise CourseFullError
        if payment:
            self.students.append(name)
            print("Enrolled:", name)


try:
    c = PaidCourse()
    c.enroll_student("A", True)
    c.enroll_student("B", True)
    c.enroll_student("C", True)

except CourseFullError:
    print("Course full! Added to waitlist")