# function to pull reviews from yelp.com using API

# API Call & Dataframe Creation
import requests
import json
import pandas as pd

# Loading API Key from .env file
from dotenv import load_dotenv
import os

# added code to pull Yelp API Key from .env file
load_dotenv()
API_AUTH = os.getenv('api_key')


def yelp_business_reviews(business_name, location):
    """
    function to pull a business's 3 most recent reviews from yelp.com and convert them to a pandas dataframe

    Args:
        business_name (str): business name on yelp.com; spelling must match spelling on yelp.com
        location (str): business's city, street address, neighborhood, or zipcode on yelp.com; spelling must match spelling on yelp.com

    Returns:
        dataframe: pandas dataframe containing business's name, yelp.com business_id, address, text excerpts from reviews of that business, yelp.com review_id, and the corresponding star ratings of the reviews from a business's 3 most-recent reviews on yelp.com


    """
    try:
        # api key from yelp fusion
        api_key = API_AUTH

        # headers, url, and parameters to pass to GET request
        headers = {'Authorization': 'Bearer {}'.format(api_key)}
        url = "https://api.yelp.com/v3/businesses/search"
        params = {
            'term': business_name.replace(' ', '+'),
            'location': location.replace(' ', '+'),
        }

        # business GET request
        req=requests.get(url, params=params, headers=headers)

        # formatting text from the response - businesses
        pretty_json = json.loads(req.content)

        # convert response into a dataframe
        # limit dataframe to business name from search
        df = pd.DataFrame(pretty_json['businesses'])
        df = df[df.name == business_name]

        # pull business' business_id from dataframe
        # located in first column of dataframe's only row
        business_id = df.iloc[0,0]

        # pull business_location to be used later
        raw_loc = df.iloc[0,12]
        business_location = str(raw_loc['address1'] + ', ' + raw_loc['city'] + ', ' + raw_loc['state'] + ' ' + raw_loc['zip_code'])

        # update URL to yelp review api
        # insert business_id from business dataframe into url string
        url = "https://api.yelp.com/v3/businesses/{}/reviews".format(business_id)

        # review GET request
        req = requests.get(url, headers=headers)

        # formatting text from response - reviews
        pretty_json = json.loads(req.content)

        # convert response into a dataframe
        # add business_name & business location to dataframe for clarity
        # drop unnecessary columns
        df = pd.DataFrame(pretty_json['reviews'])
        df['business_name'] = business_name
        df['business_id'] = business_id
        df['business_location'] = business_location
        df = df.drop(columns=['url', 'time_created', 'user'])

        # strip .html from 'text' column
        df['text'] = df['text'].str.replace('(\d{1,2}[/. ](?:\d{1,2}|January|Jan)[/. ]\d{2}(?:\d{2})?)', '')
        df['text'] = df['text'].str.replace('\n\n', '. ')                                    
        df['text'] = df['text'].str.replace('\\n', ' ')
        df['text'] = df['text'].str.replace('\n', ' ')

        # reorganize columns of dataframe
        # change 'text' column name to 'review_text'
        cols = ['business_name', 'business_id', 'business_location', 'text', 'id', 'rating']
        df = df[cols]
        df = df.rename(columns={"id": "review_id"})

        return df
    
    except:
        print('Sorry! Either name or location provided in search was not specific enough for the Yelp API.  Please try again.')

print(yelp_business_reviews("La Piazza","1137 Old Country Rd"))