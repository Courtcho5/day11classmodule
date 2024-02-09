from person import Person


class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)  # goes to previous class and calls self
        self.courses_taught = []
