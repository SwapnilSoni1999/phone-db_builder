import requests
from bs4 import BeautifulSoup
from time import sleep

DEVICES = list()

def scrape_brand(soup):
    devics = soup.find('div', { 'class': 'makers' }).find_all('li')
    # for every device found extract the info and store in list
    for d in devics:
        name = d.find('strong').text
        print("\t",name)
        href = 'https://gsmarena.com/' + d.find('a')['href']
        img = {
            'src': d.find('img')['src'],
            'desc': d.find('img')['title']
        }
        DEVICES.append({
            'name': name,
            'href': href,
            'img': img
        })

    
def next_page(soup):
    return soup.find('a', { 'class': 'pages-next', 'title': 'Next page' })

def get(brand: dict):
    """ Returns all scraped devices from brand """
    res = requests.get(brand['href'])
    print("Brand:", brand['name'])
    sleep(3)
    soup = BeautifulSoup(res.text, 'lxml')
    # do while loop it doesnt have next page
    # means first just do it
    page = 1
    scrape_brand(soup)
    has_next_page = next_page(soup)
    while bool(has_next_page):
        print("On page:", page)
        # res to next page and go
        res = requests.get('https://gsmarena.com/' + has_next_page['href'])
        sleep(3)
        next_soup = BeautifulSoup(res.text, 'lxml')
        try:
            scrape_brand(next_soup)
        except: pass
        has_next_page = next_page(next_soup)
        page += 1
        
    return DEVICES
        