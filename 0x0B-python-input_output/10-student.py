class Student:
    """Defines a student."""
    def __init__(self, first_name, last_name, age):
        """Instantiates a Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation

        Args:
            attrs (list): A list of strings representing

        Returns:
            dict: A dictionary
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
