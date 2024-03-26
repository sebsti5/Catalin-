class Student:
    def __init__(self, first_name, last_name, email, faculty):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.faculty = faculty
        self.graduated = False

    def is_graduated(self):
        return self.graduated


class StudyField:
    def __init__(self, name):
        self.name = name


class Faculty:
    student_list = []
    faculties = []

    def __init__(self, name, abbreviation, study_field):
        self.name = name
        self.abbreviation = abbreviation
        self.study_field = study_field
        self.students = []
        self.graduates = []
        Faculty.faculties.append(self)

    @staticmethod
    def get_faculty_by_abbreviation(abbreviation):
        for faculty in Faculty.faculties:
            if faculty.get_abbreviation() == abbreviation:
                return faculty
        return None

    @staticmethod
    def display_student_faculty(email):
        for student in Faculty.student_list:
            if student.email == email:
                print(f"{student.first_name} {student.last_name} belongs to the {student.faculty.name} faculty.")

    @staticmethod
    def display_all_faculties():
        print("Here are all the faculties:")
        for faculty in Faculty.faculties:
            print(f"Name: {faculty.name}, Abbreviation: {faculty.abbreviation}, Study Field: {faculty.study_field.name}")

    @staticmethod
    def display_all_faculties_of_a_field(study_field):
        print(f"Here are all the faculties belonging to {study_field.name}")
        for faculty in Faculty.faculties:
            if faculty.study_field == study_field:
                print(faculty.name)

    def create_student(self, student):
        self.students.append(student)
        print(f"{student.first_name} {student.last_name} was added to the student list")
        student.graduated = False
        print(student.graduated)

    @staticmethod
    def graduate_student(email):
        for student in Faculty.student_list:
            if student.email == email:
                print(f"{student.first_name} {student.last_name} has graduated from: {student.faculty.name}")
                student.graduated = True

    @staticmethod
    def display_students(abbreviation, is_graduated):
        for student in Faculty.student_list:
            if student.faculty.abbreviation == abbreviation and not student.is_graduated() and not is_graduated:
                print(f"{student.first_name} {student.last_name}")
            elif student.faculty.abbreviation == abbreviation and student.is_graduated() and is_graduated:
                print(f"{student.first_name} {student.last_name}")

    @staticmethod
    def is_student_from_faculty(abbreviation, email):
        for student in Faculty.student_list:
            if student.faculty.abbreviation == abbreviation and student.email == email:
                print("Student does belong to faculty")
                return
        print("Student does not belong to faculty")

    def get_students(self):
        return self.students

    def get_name(self):
        return self.name

    def get_abbreviation(self):
        return self.abbreviation

    def get_study_field(self):
        return self.study_field


# Example usage:
math_field = StudyField("Mathematics")
cs_faculty = Faculty("Computer Science Faculty", "CSF", math_field)

student1 = Student("John", "Doe", "john.doe@email.com", cs_faculty)
cs_faculty.create_student(student1)
Faculty.display_all_faculties()
Faculty.display_all_faculties_of_a_field(math_field)
Faculty.display_student_faculty("john.doe@email.com")
    