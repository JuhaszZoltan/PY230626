CURRENT_YEAR:int = 2023

DRIVER_RATE_PER_HOUR:int = 3950
PRICE_PER_KM:int = 165
CONSUMPTION_RATE:float = 6.3

# in HUF, source: https://holtankoljak.hu/ | 2023-06-26 ~11:20
DIESEL_PRICE:float = 566.6

# in Km and hour, sorce: google maps, 2023-06-26 ~11:20
BUDAPEST_DEBRECEN_DISTANCE:int = 233
BUDAPEST_DEBRECEN_DELTATIME:float = 2.4

BUDAPEST_MISKOLC_DISTANCE:int = 187
BUDAPEST_MISKOLC_DELTATIME:float = 2.1

DEBRECEN_MISKOLC_DISTANCE:int = 115
DEBRECEN_MISKOLC_DELTATIME:float = 1.3


class TransitPrices:
    def __init__(self, capita:int, reveneu:int) -> None:
        self.capita:int = capita
        self.revenue:int = reveneu


def price_calculation(origination:str, destination:str, number_of_passengers:int) -> TransitPrices:
    origination = origination.lower()
    destination = destination.lower()
    if origination[0] > destination[0]: origination, destination = destination, origination
    if (origination, destination) == ('budapest', 'debrecen'):
        distance = BUDAPEST_DEBRECEN_DISTANCE
        time = BUDAPEST_DEBRECEN_DELTATIME
    elif (origination, destination) == ('budapest', 'miskolc'):
        distance = BUDAPEST_MISKOLC_DISTANCE
        time = BUDAPEST_MISKOLC_DELTATIME
    elif (origination, destination) == ('debrecen', 'miskolc'):
        distance = DEBRECEN_MISKOLC_DISTANCE
        time = DEBRECEN_MISKOLC_DELTATIME
    else:
        print('ERROR: something went wrong')
        return None

    road_price:float = distance * PRICE_PER_KM
    fuel_cost:float = distance/100 * CONSUMPTION_RATE * DIESEL_PRICE
    total_price:float = road_price + (time * DRIVER_RATE_PER_HOUR)

    return TransitPrices(
        capita=round(total_price / number_of_passengers), 
        reveneu=round(road_price - fuel_cost))


class Product:
    def __init__(self, datarow:str) -> None:
        datasplits:list[str] = datarow.strip().split(';')
        self.name:str = datasplits[0]
        self.price:int = int(datasplits[1])
        self.stock:int = int(datasplits[2])