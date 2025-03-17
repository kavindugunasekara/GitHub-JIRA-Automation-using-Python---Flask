# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://kavindugunasekara2000-1740483750696.atlassian.net/rest/api/3/issue"

API_TOKEN ="ATATT3xFfGF0tPFoWu_grJjeUD22MLAEmRvyHClnBAt9moqjzfzJxyuKiUOXBFCrHp6EqFKwzb6hBDAIpNjQEyuyvS18jKoTPjVF7RcMmZRCLrKPm6HTMwXiAHwAUUzDkgJCpXWK3KQjolyavETY5nuwne-FYEfiljSM7W9Jjna1JaLtg5-gbN0=6B18BC59"

auth = HTTPBasicAuth("kavindugunasekara2000@gmail.com", API_TOKEN  )

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10003"
    },
    
    "project": {
      "key": "SCRUM"
    },
    
    "summary": "First JIRA ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))