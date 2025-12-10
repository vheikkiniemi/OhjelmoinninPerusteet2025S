import time

class Dog:
    def __init__(self, name, age, pituus, hinta ):
        self.name = name      # attribute
        self.age = age        # attribute
        self.pituus = pituus
        self.hinta = hinta

    def bark(self):           # method
        print(f"{self.name} barks! {self.pituus}")

    def universaali(self):
        return f"{self.hinta:.2f}"

    def suomiMuunnos(self):
        return f"{self.hinta:.2f}".replace('.',',') + " €"

def main():
    my_dog = Dog("Max", 5, 100, 10.50)
    #my_dog.bark()
    print(my_dog.universaali())
    print(my_dog.suomiMuunnos())

if __name__ == "__main__":
    main()
