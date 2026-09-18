
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def __str__(self):
        return f"{self.student_id}: {self.name}"


class Teacher:
    def __init__(self, teacher_id, name):
        self.teacher_id = teacher_id
        self.name = name
        self.course_instances = []

    def add_course_instance(self, course_instance):
        """Assign this teacher to a course instance."""
        if course_instance not in self.course_instances:
            self.course_instances.append(course_instance)
            course_instance.teacher = self

    def add_student(self, course_instance, student):
        """Add a student to a course instance."""
        if course_instance not in self.course_instances:
            raise PermissionError(
                "Teacher is not assigned to this course instance."
            )

        course_instance.add_student(student)

    def give_grade(self, course_instance, student, grade):
        """Give a grade to a student in a course instance."""
        if course_instance not in self.course_instances:
            raise PermissionError(
                "Teacher is not assigned to this course instance."
            )

        course_instance.set_grade(student, grade)

    def view_all_grades(self, course_instance):
        """View all grades for the teacher's course instance."""
        if course_instance not in self.course_instances:
            raise PermissionError(
                "Teacher is not assigned to this course instance."
            )

        return course_instance.get_all_grades()

    def view_student_grade(self, course_instance, student):
        """View one student's grade."""
        if course_instance not in self.course_instances:
            raise PermissionError(
                "Teacher is not assigned to this course instance."
            )

        return course_instance.get_grade(student)

    def __str__(self):
        return f"{self.teacher_id}: {self.name}"


class Course:
    def __init__(self, course_code, name):
        self.course_code = course_code
        self.name = name
        self.course_instances = []

    def add_instance(self, course_instance):
        self.course_instances.append(course_instance)

    def __str__(self):
        return f"{self.course_code}: {self.name}"


class CourseInstance:
    def __init__(self, instance_id, course, semester):
        self.instance_id = instance_id
        self.course = course
        self.semester = semester
        self.teacher = None

        # Dictionary:
        # student -> grade
        # None means the student has not received a grade yet.
        self.students = {}

        course.add_instance(self)

    def add_student(self, student):
        """Enroll a student."""
        if student in self.students:
            raise ValueError("Student is already enrolled.")

        self.students[student] = None

    def set_grade(self, student, grade):
        """Set a grade for an enrolled student."""
        if student not in self.students:
            raise ValueError("Student is not enrolled in this course instance.")

        if not isinstance(grade, (int, float)):
            raise TypeError("Grade must be a number.")

        if grade < 0 or grade > 5:
            raise ValueError("Grade must be between 0 and 5.")

        self.students[student] = grade

    def get_grade(self, student):
        """Return one student's grade."""
        if student not in self.students:
            raise ValueError("Student is not enrolled in this course instance.")

        return self.students[student]

    def get_all_grades(self):
        """Return all students and their grades."""
        return {
            student.name: grade
            for student, grade in self.students.items()
        }

    def __str__(self):
        teacher_name = self.teacher.name if self.teacher else "No teacher"

        return (
            f"{self.instance_id}: {self.course.name} "
            f"({self.semester}) - Teacher: {teacher_name}"
        )


class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_course(self, course):
        self.courses.append(course)

    def __str__(self):
        return self.name