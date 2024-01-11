class Dog:
    count = 0

    def __init__(self, name="unknown"):
        self.name = name
        Dog.count += 1

    @classmethod
    def get_all_dog_count(cls):
        return cls.count

    @classmethod
    def get_breed_count(cls):
        return cls.count

    def sleep(self):
        return "zzz"

    def __str__(self):
        return self.name


class Boxer(Dog):
    count = 0

    def __init__(self, name="unknown"):
        Boxer.count += 1
        super().__init__(name)

    def greet(self):
        return f"The name's {self.name}. Pleasure."

    @classmethod
    def get_characteristics(cls):
        return "Boxers are lovers, not fighters."

    def __repr__(self):
        return f"Boxer('{self.name}')"


class Puggle(Dog):
    count = 0

    def __init__(self, name="unknown"):
        Puggle.count += 1
        super().__init__(name)

    def greet(self):
        return f"I am {self.name}. I am SO HAPPY to meet you!"

    @classmethod
    def get_characteristics(cls):
        return "Like a mini boxer"

    def __repr__(self):
        return f"Puggle('{self.name}')"


class DogPack:
    instances = []

    def __init__(self, dogs=None):
        self.dogs = dogs or []
        self.instances.append(self)

    def __str__(self):
        return " ".join([str(dog) for dog in self.dogs])

    def __repr__(self):
        dog_reprs = repr(self.dogs)
        return f"DogPack({dog_reprs})"

    def callout(self):
        return [dog.greet() for dog in self.dogs]

    @staticmethod
    def describe():
        return 'A DogPack is "composed" of Dog instances.'
