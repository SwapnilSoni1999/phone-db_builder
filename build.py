import brands
import devices
import json
import os
# initiate scraper and get all brands
FINAL_DATA = list()

def save():
    if os.path.exists('phone_data.json'):
        print('Updating file...')
        os.remove('phone_data.json')
        json.dump(FINAL_DATA, open('phone_data.json', 'w'), indent=4)
        print('Updated!')
    else:
        print('Saving to file...')
        json.dump(FINAL_DATA, open('phone_data.json', 'w'), indent=4)
        print('Saved!')


brands = brands.get()
# for each brand get devices
for brand in brands:
    d = devices.get(brand)
    FINAL_DATA.append({
        'name': brand['name'],
        'device_count': brand['device_count'],
        'href': brand['href'],
        'devices': d
    })
    save()

print("Scraping Data Finished!!!")
if os.path.exists('phone_data.json'):
    os.remove('phone_data.json')
json.dump(FINAL_DATA, open('phone_data.json', 'w'), indent=4)
print("Saved File!")