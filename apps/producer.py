import requests
import random as rd 
import time
import json

from env_contraints import stream_name, fake_user_api_url, client

def get_data():
    response_user = requests.get(fake_user_api_url).json()
    response_user_results = response_user['results'][0]

    user_name = response_user_results['name']['first'] + ' ' + response_user_results['name']['last']
    user_city = response_user_results['location']['city']
    pointsMade = rd.randrange(1,200)
    #sends generated datas to be sent in points_data 

    points_data = {
        'name': user_name,
        'city': user_city,
        'points': pointsMade,
    }

    client.put_record(
        StreamName = stream_name,
        Data = json.dumps(points_data),
        PartitionKey = '02'
    )
   
    return points_data
