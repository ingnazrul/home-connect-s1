
class Internet ():
    def __init__(self, brand : str, model: str) -> None:
        self.brand = brand
        self.model = model

    def connect(self):
        connection_str = f"{self.brand}:{self.model} is connected!"
        print(connection_str)

        

if __name__ == "__main__":
    print(Internet)
    o2_fast_internet = Internet(brand="O2", model="FastInternet")
    o2_fast_internet.connect()

