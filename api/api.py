# initial exploration into Yelp's API

import requests
import json
import pandas as pd

# API key and headers
api_key = ''
headers = {'Authorization': 'Bearer %s' % api_key}

### API CALL TO GET BUSINESS INFO ###

# GET request url + search parameters
url1 = "https://api.yelp.com/v3/businesses/search"
params = {'name':'Pelham Pizza', 'location':'Pelham'}

# GET request
# req=requests.get(url1, params=params, headers=headers)
# # proceed only if the status code is 200
# print('The status code is {}'.format(req.status_code))
# # printing the text from the response 
# pretty_json = json.loads(req.text)
# print(json.dumps(pretty_json, indent=2))


### API CALL TO PULL 3 REVIEWS FROM A GIVEN BUSINESS ###

# GET request url
url2 = "https://api.yelp.com/v3/businesses/50MhEjUPvlzitewauqsqYQ/reviews"

# GET request
req2 = requests.get(url2, headers=headers)
# proceed only if the status code is 200
# print('the status code is {}'.format(req2.status_code))

pretty_json = json.loads(req2.text)
print(json.dumps(pretty_json, indent=2))


# EXPERIMENTATION WITH CONVERTING API CALL TO PANDAS DATAFRAME

# df = pd.DataFrame(pretty_json['reviews'])
# print(df)