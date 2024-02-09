from person import Person


class student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.courses_taught = []
