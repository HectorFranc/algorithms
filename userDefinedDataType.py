class Student:
    def __init__(self, uid, name, age, courses):
        self.uid = int(uid)
        self.name = str(name)
        self.age = int(age)
        self.courses = list(courses)


if __name__ == '__main__':
    student1 = Student(1, 'Hector', 14, ['Programming', 'English'])
    print('Name:', student1.name, ', Age:', student1.age, ', Courses:')
    for course in student1.courses:
        print('-', course)
