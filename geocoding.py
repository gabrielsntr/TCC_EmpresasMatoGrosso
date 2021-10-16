import requests
import urllib

#key = 'AmT5hFiQNspOAiPhBcxXdHhwxxotzX5N'
base_url = 'https://photon.komoot.io/api/'

address = {
    'street_ad': '235, Rua Das Azaleias',
    'city': 'Sinop',
    'state': 'Mato Grosso',
    'country': 'Brazil'
}

params = {
    'q': '235, Rua Das Azaleias, Sinop, Mato Grosso, Brazil' #urllib.parse.quote('235, Rua Das Azaleias, Sinop, Mato Grosso, Brazil', safe='')
}
print(params['q'])
resp = requests.get(base_url, params=params)
print(resp.status_code)
print(resp.json())