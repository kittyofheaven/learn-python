import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Surabaya&AreaID=501306&Prov=35')
soup = BeautifulSoup(page.content, 'html.parser')

cuaca = soup.find_all(class_='prakicu-kabkota')