
import requests

API_KEY = 'eeef357467bd0f55cf650632a5ceab04'
sport = 'icehockey_nhl'
url = f'https://api.the-odds-api.com/v4/sports/{sport}/odds/?apiKey={API_KEY}&regions=us&markets=h2h,spreads&oddsFormat=american'

response = requests.get(url)
data = response.json()

print(data)