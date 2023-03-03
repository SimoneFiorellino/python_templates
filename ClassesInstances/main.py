from student import Student

if __name__ == "__main__":
    new_student = Student(
        name = 'Mario',
        surname = 'Rossi',
        age = 20
    )
    new_student.print()

    print('\n')

    print(Student.__dict__)
    print(new_student.__dict__)

    print('\n')

    # call class attribute
    print(new_student.university)
    print(Student.university)

    print('\n')

    # call instance attribute
    print(new_student.name)

    print('\n')

    # change class attribute
    Student.university = 'Roma Tre'
    print(new_student.university)

    print('\n')

    # change instance attribute
    new_student.name = 'Luigi'
    print(new_student.name)

    print('\n')

    # delete instance attribute
    del new_student.name
    print(new_student.__dict__)

    print('\n')

    # delete class attribute
    del Student.university
    print(Student.__dict__)

    print('\n')

    # call functions
    new_student.name = 'Mario'
    new_student.hello()

    print('\n')

    # call class method
    print(new_student.role)

    print('\n')

    # call static method
    print(new_student.stati_info())
    print(Student.stati_info())

    print('\n')

    # call dunder method
    new_student2 = Student(
        name = 'Luigi',
        surname = 'Bianchi',
        age = 20
    )
    print(new_student + new_student2)
