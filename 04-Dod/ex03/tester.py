from new_student import Student


def test_student():
    student = Student(name="Edward", surname="agle")
    print(student)

    id_test = Student(name="Edward", surname="agle", id="test")
    print(id_test)


test_student()
