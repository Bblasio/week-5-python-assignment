# Parent Class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.__storage = storage   # private attribute (encapsulation)

    # Getter method for storage
    def get_storage(self):
        return self.__storage

    # Setter method for storage
    def set_storage(self, storage):
        self.__storage = storage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.__storage}GB")


# Child Class (Inheritance)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)  # initialize parent attributes
        self.gpu = gpu

    def play_game(self, game):
        print(f"{self.brand} {self.model} with {self.gpu} is playing {game}!")


# Example usage
phone1 = Smartphone("Samsung", "Galaxy S25 Ultra", 128)
phone1.info()
phone1.call("+254712345678")

gaming_phone = GamingPhone("Asus", "ROG Phone 6", 256, "Adreno 730")
gaming_phone.info()
gaming_phone.play_game("eFOOTBALL")
