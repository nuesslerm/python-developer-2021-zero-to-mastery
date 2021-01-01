if __name__:
    print(__name__)

    def multiply(num1, num2):
        return num1 * num2

    def divide(num1, num2):
        return num1 / num2

    # def max():
    #     print("joooo")

    if __name__ == "__main__":
        print("AHHHHHHH")

    class Student:
        pass

    student = Student()

    # if run in this file gives <class '__main__.Student'>
    # if run in test file gives <class 'utility.Student'>
    print(type(student))