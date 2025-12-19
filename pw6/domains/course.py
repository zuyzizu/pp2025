class Course:
    def __init__(self):
        self._id = ""
        self._name = ""
        self._credit = 0

    def input(self):
        self._id = input("Course ID: ")
        self._name = input("Course Name: ")
        self._credit = int(input("Course Credit: "))

    def list(self):
        return f"ID: {self._id} | Name: {self._name} | Credit: {self._credit}"

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_credit(self):
        return self._credit

