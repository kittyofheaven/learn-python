import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.09976000000006&lon=-118.33197499999994')
soup = BeautifulSoup(page.content, 'html.parser')
week =  soup.find(id='seven-day-forecast-body')

#print(week)
items = week.find_all(class_='tombstone-container') #buat access class

#print(type(items))

#l = []
#for x in range(9) :
    #l.append(items[x].find(class_='period-name').get_text())
    #l.append(items[x].find(class_='short-desc').get_text())
    #l.append(items[x].find(class_='temp').get_text())
#print(l)

period_names = [item.find(class_='period-name').get_text() for item in items ]
short_desc = [item.find(class_='short-desc').get_text() for item in items ]
temperature = [item.find(class_='temp').get_text() for item in items ]

print(period_names)
print(short_desc)
print(temperature)
