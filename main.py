import requests
from bs4 import BeautifulSoup
from emailtool import send_email


URL = "https://www.brasiltronic.com.br/camera-digital-fujifilm-gfx-50r-medio-formato-somente-corpo"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

site = requests.get(URL, headers=headers)

soup = BeautifulSoup(site.content, "html.parser")

title = soup.find("h1", class_="product-name").get_text()

current_price = soup.find('input', id='preco_atual')
current_price = float(current_price["value"])

if current_price < 30000:
    send_email()
