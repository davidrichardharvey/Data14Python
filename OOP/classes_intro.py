name = "David"

class Dog:

    def __init__(self, name):  # Initialisation (runs on Instantiation)
        self.name = name
        self.legs = 4
        self.animal_kind = "canine"
        self._secret = "I can't eat chocolate" # Private variable

    def __bark(self):
        return "WOOF!"

    def greeting(self):
        return f"Woof!  My name is {self.name}"

    def get_secret(self):  # GETTER
        return self._secret

    def set_secret(self, secret):  # SETTER
        self._secret = secret

new_dog = Dog("Lassie")

print(new_dog.get_secret())
new_dog.set_secret("I hid my bone in the garden")
print(new_dog.get_secret())