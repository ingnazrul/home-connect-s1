from src.internet import Internet
from src.television import Television
from src.aircondition import Aircondition
from src.homeAssistance import Homeassistance


def main():
    o2_fast_internet = Internet(brand="O2", model="FastInternet")
    samsung_odc= Television(brand= "samsung", model="odessy")
    general_air=Aircondition(brand="General" , model = "CooleAde")
    home_ass = Homeassistance(brand = "Amazon" , model = "Alexa")
    o2_fast_internet.connect()
    samsung_odc.connect()
    general_air.connect()
    home_ass.connect()



if __name__ == "__main__":
    print(Internet)
    main()

