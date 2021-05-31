# https://cdn-api.co-vin.in/api/v2​/appointment​/sessions​/public​/findByDistrict

import requests

base_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict"
dist_id = 49
date = "31-05-2021"

# Send to telegram
group_id = '-543656097'



while True:
    final_url = f'{base_url}?district_id={dist_id}&date={date}'
    response = requests.get(final_url)
    print(response)
    print(response.text)
