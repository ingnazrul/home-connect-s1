class Homeassistance ():
    def __init__(self, brand : str, model: str) -> None:
        self.brand = brand
        self.model = model

    def connect(self):
        connection_str = f"{self.brand}:{self.model} is connected!"
        print(connection_str)