
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('API_KEY')

sport = 'icehockey_nhl'
url = f'https://api.the-odds-api.com/v4/sports/{sport}/odds/?apiKey={API_KEY}&regions=us&markets=h2h,spreads&oddsFormat=american'

response = requests.get(url)
data = response.json()

print(data)