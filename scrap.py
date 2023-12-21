from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL to be scraped
url = 'https://resultados.as.com/resultados/futbol/primera/clasificacion/'

# Get the HTML content
page = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(page.content, 'html.parser')

# Equipos

eq = soup.find_all('span', class_='nombre-equipo')

equipos = list()

# Get the text of each team
count = 0
for i in eq:
    if count < 20:
        equipos.append(i.text)
    else:
        break
    count += 1

# Puntos
    
pt = soup.find_all('td', class_='destacado')

puntos = list()

# Get the text of each team
count = 0
for i in pt:
    if count < 20:
        puntos.append(i.text)
    else:
        break
    count += 1

# Partidos jugados

pj = soup.find_all('td', class_='')

partidos_jugados = list()

# Get the text of each team

count = 0
for i in pj:
    if count < 20:
        partidos_jugados.append(i.text)
    else:
        break
    count += 1

# Partidos ganados
    
pg = soup.find_all('td', class_='')

partidos_ganados = list()

# Get the text of each team

count = 0
for i in pg:
    if count < 20:
        partidos_ganados.append(i.text)
    else:
        break
    count += 1

# Partidos empatados
    
pe = soup.find_all('td', class_='')

partidos_empatados = list()

# Get the text of each team

count = 0
for i in pe:
    if count < 20:
        partidos_empatados.append(i.text)
    else:
        break
    count += 1

# Partidos perdidos
    
pp = soup.find_all('td', class_='')

partidos_perdidos = list()

# Get the text of each team

count = 0
for i in pp:
    if count < 20:
        partidos_perdidos.append(i.text)
    else:
        break
    count += 1

# Hacer un csv con los datos separados por columnas y filas

df = pd.DataFrame({'Equipo': equipos, 'Puntos': puntos, 'Partidos jugados': partidos_jugados, 'Partidos ganados': partidos_ganados, 'Partidos empatados': partidos_empatados, 'Partidos perdidos': partidos_perdidos})

df.to_csv('clasificacion.csv', index=False, encoding='utf-8')



