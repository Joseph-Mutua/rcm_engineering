import requests
import json
from pprint import pprint

apiKey = "c9sdv8qad3i4aps1sleg"

symbol = "DAL"

base_url = "https://finnhub.io/api/v1/stock/profile2?"
r = requests.get(baseurl, params = {'symbol':symbol,'token':apiKey}
text = r.text
company_profile = json.loads(text)

pprint(company_profile)