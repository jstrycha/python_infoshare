import os
import requests
from bs4 import BeautifulSoup
from PIL import Image

adres_strony = 'https://www.olx.pl/motoryzacja/samochody/'

#pobieramy źródło strony do zmiennej
zrodlo_strony = requests.get(adres_strony).content

#tworzymy parser BeautifulSoup z podanego źródła strony dzięki temu będziemy mieli łatwy dostęp do znaczników HTML
parser = BeautifulSoup(zrodlo_strony, 'html.parser')

# pobieramy źródło strony
response = requests.get(adres_strony)
parser = BeautifulSoup(response.content, 'html.parser')

# pobieramy tylko linki HTTPS do obrazków
images_links = {}
for img in parser.find_all('img'):
    src = img.get('src')
    if src and src.startswith("https"):
        images_links[img.get('alt')] = img.get('src')

print(images_links)

# tworzymy folder na obrazki
os.makedirs("../pobrane_obrazki", exist_ok=True)

# zapisywanie plików
for name, url in images_links.items():
    try:
        img_data = requests.get(url).content
        name = name.replace('/','-').replace(' ','-')
        path = f"pobrane_obrazki/{name}.jpg"
        with open(path, 'wb+') as file:
            file.write(img_data)
            print("Utworzono nowy plik")

    except Exception as e:
        print(f"Błąd przy pobieraniu {url}: {e}")