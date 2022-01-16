import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://www.koronavirus.hr/json/?action=po_danima_zupanijama_zadnji"
data = requests.get(url).json()

regions = []
active_cases = []
deaths = []

for zupanija in data['PodaciDetaljno']:
    regions.append(zupanija['Zupanija'])
    active_cases.append(zupanija['broj_aktivni'])
    deaths.append(zupanija['broj_umrlih'])

def cases_per_regions(self):
    plt.barh(regions, active_cases)
    plt.xlabel("Number of active cases")
    plt.ylabel("Region")
    plt.title("Covid-19 active cases by region")
    plt.show()

def deaths_per_regions(self):
    plt.barh(regions, deaths)
    plt.xlabel("Number of deaths")
    plt.ylabel("Region")
    plt.title("Covid-19 deaths by region")
    plt.show()

def sum_cases(self):
    num_of_cases = [elem['broj_aktivni'] for elem in data['PodaciDetaljno']]
    return sum(num_of_cases)

def last_info(self):
    urldva = 'https://www.koronavirus.hr/json/?action=podaci_zadnji'
    data = requests.get(urldva).json()
    umrliHr = data['UmrliHrvatska']
    return umrliHr

def updated_date(self):
    urldva = 'https://www.koronavirus.hr/json/?action=podaci_zadnji'
    data = requests.get(urldva).json()
    date = data['lastUpdated']
    return date

def urmli_zarazeni(self):
    df = pd.DataFrame({'Active cases': active_cases, 'Deaths': deaths}, index=regions)
    df.plot.barh()
    plt.show()

def deaths_per_population(self):
    population = [102295, 130782, 115862, 769944, 195794, 112596, 101661, 120942, 42893, 105863, 259481, 64420, 266503, 96624, 140549, 425412, 160264, 144438, 160340, 301206]
    new_deaths = []

    for zupanija in data['PodaciDetaljno']:
        new_deaths.append(zupanija['broj_umrlih'])

    for i in range (0, 20):
        x = population[i] / 100000
        new_deaths[i] = new_deaths[i] / x

    plt.barh(regions, new_deaths)
    plt.xlabel("Number of death cases per 100.000 people ")
    plt.ylabel("Region")
    plt.title("Covid-19 death cases (per 100.000 people) by region")
    plt.show()
