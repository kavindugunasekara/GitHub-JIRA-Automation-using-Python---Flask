from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json
app = Flask(__name__) #creating a flask applction instance

#Decorator for the route  (decorator performs an action before the execution of the function the use of The Decorator is
# whenever someone is trying to access this particular API okay so here in terms of flask it is doing two things one flask it is doing two things one is it
#is saying flask that okay only surf particular function on this particular
#lash if someone is trying to slash if someone is trying to access it
#on a different URL then send out this particular error message that we are seeing
@app.route("/createJIRA", methods=['POST'])
def createJIRA():
 

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

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))


if __name__ == '__main__':
#need a server what flas does is flask creates an inbuilt server which is Flash server
    app.run('0.0.0.0', port=5000)