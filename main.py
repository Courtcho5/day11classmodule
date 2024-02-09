import module
from module import sayhello
from person import Person
from teacher import Teacher
from course import Course

if __name__ == '__main__':  # __name__ references call environment
    a_person = Person("Fred Smith")
    print(a_person.name)
    hcde_teacher = Teacher("Adrian Rodriguez")
    print(hcde_teacher.name)
    hcde_class = Course("HCDE 310:", hcde_teacher)
    print(hcde_class.teacher.name)

    for course in hcde_teacher.courses_taught:
        print(course.name)
print(f"Teacher: {hcde_teacher.name} is teaching {hcde_teacher.courses_taught[0].name}")
