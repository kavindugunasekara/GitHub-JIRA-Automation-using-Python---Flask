# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://kavindugunasekara2000-1740483750696.atlassian.net/rest/api/3/project"

API_TOKEN ="ATATT3xFfGF0tPFoWu_grJjeUD22MLAEmRvyHClnBAt9moqjzfzJxyuKiUOXBFCrHp6EqFKwzb6hBDAIpNjQEyuyvS18jKoTPjVF7RcMmZRCLrKPm6HTMwXiAHwAUUzDkgJCpXWK3KQjolyavETY5nuwne-FYEfiljSM7W9Jjna1JaLtg5-gbN0=6B18BC59"

auth = HTTPBasicAuth("kavindugunasekara2000@gmail.com", API_TOKEN  )

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]['name']

print(name)