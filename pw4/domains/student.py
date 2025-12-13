class Student:
    def __init__(self):
        self._id = ""
        self._name = ""
        self._dob = ""

    def input(self):
        self._id = input("ID: ")
        self._name = input("Name: ")
        self._dob = input("Date of Birth (DoB): ")

    def list(self):
        return f"ID: {self._id} | Name: {self._name} | DoB: {self._dob}"

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

