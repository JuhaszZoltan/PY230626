from module import *

# --- 1st exercise ---
year_of_birth:int = int(input('enter your year of birth: '))
if CURRENT_YEAR < year_of_birth: print("ERROR: something went wrong")
else: print(f'you will be {CURRENT_YEAR - year_of_birth} years old this year')
print('------------------------')

# --- 2nd exercise ---
origin_city:str = input('the name of the city you are starting from: ')
dest_city:str = input('the name of the city you are arriving in: ')
no_passengers:int = int(input('the number of passengers: '))
tps = price_calculation(origin_city, dest_city, no_passengers)
if tps is not None:
    print(f'the price of the trip per person: {tps.capita} HUF')
    print(f'the turnover of the business: {tps.revenue} HUF')
print('------------------------')

# --- 3rd exercise ---
vm:list[Product] = []
for row in open('vm2023.txt', 'r', encoding='utf-8'): vm.append(Product(row))
print(f'3.1: temékek száma: {len(vm)}')
price_sum:int = 0
upto_200:int = 0
max_index:int = 0
for product in vm:
    price_sum += (product.price * product.stock)
    if product.price <= 200: upto_200 += 1
    if vm[max_index].price < product.price: max_index = vm.index(product)
print(f'3.2: termékek összértéke: {price_sum} HUF')
print(f'3.3: 200 HUF-ból megvásárolható termékek száma: {upto_200} db')
print('3.4: legdrágább termék:')
print(f'\tnév: {vm[max_index].name}')
print(f'\tár: {vm[max_index].price} HUF')
print(f'\tkészlet: {vm[max_index].stock} db')
searched_name:str = input(f'3.5 írd be a keresett termék nevét: ').lower()
for product in vm:
    if searched_name == product.name.lower():
        print(f'\tár: {product.price} HUF')
        print(f'\tkészlet: {product.stock} db')
        break
else: print('\tnincs ilyen nevű termék!')
