import requests
from pprint import pprint


url = "http://api.stackexchange.com//2.3/questions?fromdate=1658620800&todate=1658793600&order=desc&mi" \
          "n=1658620800&max=1658793600&sort=activity&tagged='Python'&site=stackoverflow"

response = requests.get(url)
pprint(response.text)
