class Course:
    def __init__(self, name, teacher):
        self.teacher = teacher
        self.name = name
        teacher.courses_taught.append(self)  # current course
