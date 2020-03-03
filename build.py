import brands
import devices
# initiate scraper and get all brands

brands = brands.get()
FINAL_DATA = list()

# for each brand get devices
for brand in brands:
    d = devices.get(brand)
    FINAL_DATA.append({
        'name': brand['name'],
        'device_count': brand['device_count'],
        'href': brand['href'],
        'devices': d
    })
    print(d)