import brands
import devices
import checkpoint
import json
import os
# initiate scraper and get all brands
FINAL_DATA = list()
PHONE_DATA_FILE = 'phone_data.json'

# before going check for any checkpointfile
allowed = False
catch_brand = str()
try:
    catch_brand = checkpoint.read()
    data = json.load(open(PHONE_DATA_FILE, 'r'))
    for da in data:
        FINAL_DATA.append(da)
    print(f'Added {len(data)} brands! Continuing from there...')
except: 
    # means begin from beginning
    allowed = True

def save():
    if os.path.exists(PHONE_DATA_FILE):
        print('Updating file...')
        os.remove(PHONE_DATA_FILE)
        json.dump(FINAL_DATA, open(PHONE_DATA_FILE, 'w'), indent=4)
        print('Updated!')
    else:
        print('Saving to file...')
        json.dump(FINAL_DATA, open(PHONE_DATA_FILE, 'w'), indent=4)
        print('Saved!')


brands = brands.get()
# for each brand get devices
for brand in brands:
    if (allowed == False) and (brand['name'] == catch_brand):
        allowed = True

    if allowed:
        try:
            d = devices.get(brand)
        except:
            checkpoint.add_flag(brand['name'])
            exit()
            
        FINAL_DATA.append({
            'name': brand['name'],
            'device_count': brand['device_count'],
            'href': brand['href'],
            'devices': d
        })
        save()
    else:
        print(f"Skipped {brand['name']}")

print("Scraping Data Finished!!!")
if os.path.exists(PHONE_DATA_FILE):
    os.remove(PHONE_DATA_FILE)
json.dump(FINAL_DATA, open(PHONE_DATA_FILE, 'w'), indent=4)
print("Saved File!")
checkpoint.remove()