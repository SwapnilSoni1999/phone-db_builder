import requests
from bs4 import BeautifulSoup
from time import sleep

def get():
    """ Returns all brand with { name, device_count, href } """
    res = requests.get('https://www.gsmarena.com/makers.php3')
    sleep(3)
    soup = BeautifulSoup(res.text, 'lxml')
    brands = soup.find('div', { 'class': 'st-text' }).find_all('tr')
    
    payload = list()

    # for each tr 
    for brand in brands:
        # each tr has 2 td
        for td in brand.find_all('a'):
            total_devices = td.find('span').text.split(' ')[0]
            span = td.find('span')
            span.decompose()
            print(td.text)
            payload.append({
                'name': td.text,
                'device_count': int(total_devices),
                'href': 'https://gsmarena.com/' + td['href']
            })          
    return payload

